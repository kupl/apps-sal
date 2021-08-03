from math import log

N = int(input())

dp = [0] * (N + 1)

e6 = 0
e9 = 0
for i in range(1, N + 1):
    for j in range(e6, 12):
        if 6**j > i:
            e6 = j - 1
            break
    for j in range(e9, 12):
        if 9**j > i:
            e9 = j - 1
            break
    dp[i] = min(dp[i - 1], dp[i - int(6**e6)], dp[i - int(9**e9)]) + 1

print(dp[-1])
