from collections import defaultdict
# from fractions import Fraction


def read_line():
    return [int(x) for x in input().split()]


def query(l, r):
    if l == r:
        if l % 2 == 0:
            return l
        else:
            return -r
    if l % 2 == 1:
        return -l + query(l + 1, r)
    if r % 2 == 0:
        return r + query(l, r - 1)

    num_pairs = (r + 1 - l) // 2
    sm_even = l * num_pairs + num_pairs * (num_pairs - 1)
    sm_odd = -(sm_even + num_pairs)
    return sm_even + sm_odd

# test = [i * (-1)**i for i in range(100)]
# for i in range(1, 100):
#     for j in range(i, 100):
#         print(i, j, query(i, j), sum(test[x] for x in range(i, j+1)))
#         assert query(i, j) == sum(test[x] for x in range(i, j+1))


q = int(input())
for _ in range(q):
    l, r = read_line()
    print(query(l, r))
