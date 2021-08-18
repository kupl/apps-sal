from collections import defaultdict


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


q = int(input())
for _ in range(q):
    l, r = read_line()
    print(query(l, r))
