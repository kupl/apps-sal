import sys

n, m, k = list(map(int, input().split()))
table = [input() for _ in range(n)]

dp = [0]*(k+1)

for a in table:
    one = []
    for i in range(m):
        if a[i] == '1':
            one.append(i)

    if not one:
        continue

    ni = len(one)
    subdp = [10**9] * (ni+1)
    subdp[-1] = 0

    for i in range(ni):
        for j in range(i, ni):
            subdp[ni-(j-i+1)] = min(subdp[ni-(j-i+1)], one[j]-one[i]+1)

    next_dp = [10**9]*(k+1)
    for i in range(k, -1, -1):
        for j in range(ni+1):
            if i+j > k:
                break
            next_dp[i+j] = min(next_dp[i+j], dp[i] + subdp[j])
    dp = next_dp

print(min(dp))

