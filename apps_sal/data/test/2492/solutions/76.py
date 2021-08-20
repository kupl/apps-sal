import numpy as np
(n, k) = map(int, input().split())
a_list = np.array(list(map(int, input().split())))
a_list.sort()
zero_list = a_list[a_list == 0]
minus_list = a_list[a_list < 0]
plus_list = a_list[a_list > 0]


def index_count(x):
    cnt = 0
    if x >= 0:
        cnt += len(zero_list) * n
    cnt += np.searchsorted(a_list, x // plus_list, side='right').sum()
    cnt += (n - np.searchsorted(a_list, -(-x // minus_list), side='left')).sum()
    cnt -= np.count_nonzero(a_list * a_list <= x)
    assert cnt % 2 == 0
    return cnt // 2


left = -10 ** 18
right = 10 ** 18
while left + 1 < right:
    mid = (left + right) // 2
    a = index_count(mid)
    if a >= k:
        right = mid
    else:
        left = mid
print(right)
