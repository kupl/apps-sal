md = 10**9 + 7
s = input()
dp = [[0] * 4 for _ in range(3)]
for c in s:
    if c == "A": dp[0][0] = (dp[0][0] + 1) % md
    if c == "B":
        for j in range(2): dp[1][j] = (dp[1][j] + dp[0][j]) % md
    if c == "C":
        for j in range(3): dp[2][j] = (dp[2][j] + dp[1][j]) % md
    if c == "?":
        for j in range(3): dp[2][j + 1] = (dp[2][j + 1] + dp[1][j]) % md
        for j in range(2): dp[1][j + 1] = (dp[1][j + 1] + dp[0][j]) % md
        dp[0][1] = (dp[0][1] + 1) % md
ans = 0
q = s.count("?")
for j in range(4):
    if q - j < 0: break
    ans += dp[2][j] * pow(3, q - j, md)
    ans %= md
print(ans)
