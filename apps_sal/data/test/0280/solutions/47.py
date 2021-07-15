from itertools import permutations
from bisect import bisect_left
import sys

INF = float('inf')
N, M = map(int,input().split())
W = list(map(int,input().split()))
L = [0] * M
V = [0] * M

for i in range(M):
    L[i], V[i] = map(int,input().split())

if max(W) > min(V):
    print(-1)
    return

ZIP = zip(V, L)
ZIP = sorted(ZIP)
V, L = zip(*ZIP)

R = [0] * M
R[0] = L[0]

for i in range(M-1):
    R[i+1] = max(R[i], L[i+1])

ans = float('inf')

for l in permutations(W, N):
    dp = [0] * N
    CUMSUM = [0]
    for i in l:
        CUMSUM.append(CUMSUM[-1] + i)
    for i in range(N-1):
        for j in range(i+2, N+1):
            tmp = CUMSUM[j] - CUMSUM[i]
            index = bisect_left(V, tmp)
            if index == 0:
                dp[j-1] = max(dp[j-1], dp[i])
            else:
                dp[j-1] = max(dp[j-1], dp[i] + R[index-1])
    ans = min(ans, dp[-1])
print(ans)
