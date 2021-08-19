import sys


def __starting_point():

    n, m = [int(i) for i in sys.stdin.readline().rstrip().split(' ')]
    a = [int(i) for i in sys.stdin.readline().rstrip().split(' ')]
    l = [None] * m
    for i in range(m):
        l[i] = int(sys.stdin.readline().rstrip())

    l_sorted = sorted(l)
    l_order = sorted(range(m), key=lambda k: l[k])

    # the ranks of elements in l
    l_rank = sorted(range(m), key=lambda k: l_order[k])

    # unique_elem[i] = non-duplicated elements between l_sorted[i] and l_sorted[i+1]
    unique_elem = [None] * m

    for i in range(m):
        unique_elem[i] = set(a[(l_sorted[i] - 1): (l_sorted[i + 1] - 1)]) if i < m - 1 else set(a[(l_sorted[i] - 1): n])

    # unique_elem_cumulative[i] = non-duplicated elements between l_sorted[i] and a's end
    unique_elem_cumulative = unique_elem[-1]

    # unique_elem_cumulative_count[i] = #unique_elem_cumulative[i]
    unique_elem_cumulative_count = [None] * m
    unique_elem_cumulative_count[-1] = len(unique_elem[-1])

    for i in range(m - 1):
        i_rev = m - i - 2
        unique_elem_cumulative |= unique_elem[i_rev]
        unique_elem_cumulative_count[i_rev] = len(unique_elem_cumulative)

    for i in range(m):
        idx = l_rank[i]
        print(unique_elem_cumulative_count[idx])


__starting_point()
