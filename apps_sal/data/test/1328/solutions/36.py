
import numpy as np

N, Ma, Mb = list(map(int, input().split()))
U = N * 10

dp = np.zeros((U + 1, U + 1), dtype=np.int64)
temp = np.zeros_like(dp)

INF = 10 ** 18
dp += INF
dp[0, 0] = 0

for _ in range(N):
    a, b, c = list(map(int, input().split()))
    temp[:] = dp.copy()
    temp[a:, b:] = np.minimum(temp[a:, b:], dp[:-a, :-b] + c)
    dp = temp

answer = INF
for t in range(1, 401):
    a = Ma * t
    b = Mb * t
    if max(a, b) >= U:
        break
    answer = min(answer, dp[a, b])

if answer == INF:
    answer = -1

print(answer)
