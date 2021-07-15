# from itertools import permutations
# N, M = map(int, input().split())
# W = list(map(int, input().split()))

# L = []
# V = []
# for _ in range(M):
#     l, v = map(int, input().split())
#     L.append(l)
#     V.append(v)

# # どのようにしても箸が落ちる時
# if min(W) > min(V):
#     print(-1)
#     return

# ans = float('inf')
# for v in permutations(W):
#     dp = [0] * N
#     for i in range(N):
#         for j in range(i + 1, N):
#             weight = v[i] + v[j]
#             for m in range(M):
#                 if weight > V[m]:
#                     dp[j] = max(dp[j], dp[j - 1] + L[m])
#     ans = min(ans, dp[-1])
# print(ans)

import itertools
import bisect

n, m = list(map(int, input().split()))
w = list(map(int, input().split()))
g = [list(map(int, input().split())) for _ in range(m)]
# 対価重量でソートする
g.sort(key=lambda x: x[1])

L = []
V = []
# 二分探索を利用する上で考えなくても良い橋の部分を除外する
init = 0
for i in range(m):
    if g[i][0] > init:
        L.append(g[i][0])
        V.append(g[i][1])
        init = g[i][0]

w.sort()
if w[0] > g[0][1]:
    print((-1))
    return

ans = float('inf')
for v in itertools.permutations(w):
    dp = [0] * n
    for i in range(1, n):
        cnt = v[i]
        for j in range(i - 1, -1, -1):
            cnt += v[j]
            bisect_v = bisect.bisect_left(V, cnt)
            if bisect_v - 1 >= len(L) or bisect_v - 1 < 0:
                continue
            dp[i] = max(dp[i], dp[j] + L[bisect_v - 1])
    ans = min(ans, dp[-1])
print(ans)

