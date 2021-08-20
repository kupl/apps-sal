import numpy as np
import sys
readline = sys.stdin.readline
(N, K) = list(map(int, readline().split()))
A = np.array(readline().split(), dtype=int)
nega_list = A[A < 0]
posi_list = A[A > 0]
zero_num = A[A == 0].size
nega_list = np.sort(nega_list)
posi_list = np.sort(posi_list)
nega_cnt = nega_list.size * posi_list.size
posi_cnt = (posi_list.size * posi_list.size - 1) // 2 + (nega_list.size * nega_list.size - 1) // 2
zero_cnt = zero_num * (zero_num - 1) // 2 + zero_num * (nega_list.size + posi_list.size)
if K <= nega_cnt:

    def isOkNega(x):
        return np.searchsorted(nega_list, x // posi_list, side='right').sum() >= K
    ok = 0
    ng = -10 ** 18 - 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if isOkNega(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
elif K <= nega_cnt + zero_cnt:
    print(0)
else:
    K -= nega_cnt + zero_cnt
    nega_list = np.flipud(nega_list * -1)
    self_nega = nega_list * nega_list
    self_posi = posi_list * posi_list

    def isOkPosi(x):
        nega_all = np.searchsorted(nega_list, x // nega_list, side='right')
        nega_cnt = nega_all.sum() - self_nega[self_nega <= x].size
        nega_cnt //= 2
        posi_all = np.searchsorted(posi_list, x // posi_list, side='right')
        posi_cnt = posi_all.sum() - self_posi[self_posi <= x].size
        posi_cnt //= 2
        return nega_cnt + posi_cnt >= K
    ok = 10 ** 18 + 1
    ng = 0
    while abs(ok - ng) > 1:
        mid = abs(ok + ng) // 2
        if isOkPosi(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
