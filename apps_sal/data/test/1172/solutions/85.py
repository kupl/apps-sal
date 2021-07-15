s = input().rstrip()
n = len(s)
mod = 10**9 + 7
dp = [0] * 4
dp[0] = 1

for i in range(n):
    next = [0] * 4
    if s[i] == 'A':
        next[1] += dp[0]
    elif s[i] == 'B':
        next[2] += dp[1]
    elif s[i] == 'C':
        next[3] += dp[2]
    else:
        next[1] += dp[0]
        next[2] += dp[1]
        next[3] += dp[2]
        next[0] += dp[0] * 2
        next[1] += dp[1] * 2
        next[2] += dp[2] * 2
        next[3] += dp[3] * 2
    next[0] += dp[0]
    next[1] += dp[1]
    next[2] += dp[2]
    next[3] += dp[3]

    for j in range(4):
        next[j] %= mod
    dp = next
print((dp[3]))

