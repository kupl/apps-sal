import bisect
from collections import deque

N = int(input())
A = [int(input()) for _ in range(N)]

dp = deque()
dp.append(A[0])

for i in range(1, N):
    ind = bisect.bisect_left(dp, A[i])

    if ind == 0:
        dp.appendleft(A[i])
    # elif dp[-1] < A[i]:
    #     dp[-1] = A[i]
    else:
        dp[ind - 1] = A[i]

print(len(dp))
