n = int(input())

l = [1]
l += [6**i for i in range(1, 7)]
l += [9**i for i in range(1, 6)]
l.sort()

dp = [0] * (n + 1)
for i in range(1, n + 1):
    cand = []
    for j in l:
        if i >= j:
            cand.append(dp[i - j] + 1)
    dp[i] = min(cand)

print(dp[n])
