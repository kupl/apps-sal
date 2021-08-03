line = input()

dp = 3 * [0]

for c in line:
    if c == 'a':
        dp[2] = max(dp) + 1
        dp[0] += 1
    elif c == 'b':
        dp[1] = max(dp[:2]) + 1

print(max(dp))
