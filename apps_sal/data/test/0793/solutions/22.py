from collections import deque
from itertools import repeat
MOD = 10 ** 9 + 7
(N, M) = map(int, input().split())
S = tuple(map(int, input().split()))
T = tuple(map(int, input().split()))
if N < M:
    (N, M) = (M, N)
    (S, T) = (T, S)
dp = deque(repeat(1, M + 1), M + 2)
for s in S:
    dp.append(1)
    for t in T:
        if s == t:
            dp.append(dp[1] + dp[-1])
        else:
            dp.append(dp[1] - dp[0] + dp[-1])
print(dp[-1] % MOD)
