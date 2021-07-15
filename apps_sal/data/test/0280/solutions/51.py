import sys
from itertools import permutations
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = list(map(int, input().split()))
    W = list(map(int, input().split()))
    LV = [list(map(int, input().split())) for _ in range(m)]

    max_w = max(W)
    min_v = min([LV[i][1] for i in range(m)])
    if min_v < max_w:
        print((-1))
        return

    LV.sort(key=lambda x: x[1])
    L = [0, LV[0][0]]
    V = [0, LV[0][1]]
    for l, v in LV[1:]:
        if l <= L[-1]:
            continue
        else:
            L.append(l)
            V.append(v)

    L.append(L[-1])
    V.append(f_inf)

    res = f_inf
    for pattern in permutations(W):
        dp = [0] * n
        for i in range(n):
            sum_w = pattern[i]
            for j in range(i + 1, n):
                sum_w += pattern[j]
                idx = bisect_left(V, sum_w)
                dp[j] = max(dp[j], dp[i] + L[idx - 1])
        res = min(res, dp[-1])
    print(res)


def __starting_point():
    resolve()

__starting_point()
