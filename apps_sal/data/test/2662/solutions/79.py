import bisect

N = int(input())
A = [int(input()) for _ in range(N)]

A.reverse()

dp = [A[0]]

for a in A[1:]:
    idx = bisect.bisect_right(dp, a)
    if idx == len(dp):
        dp.append(a)
    else:
        dp[idx] = a

print(len(dp))
