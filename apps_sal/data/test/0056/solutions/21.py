from fractions import Fraction

inp = input().split()
N, T = int(inp[0]), int(inp[1])

if T is 0:
    print(0)
    return

dp = []
for r in range(N + 1):
    dp.append([Fraction(0) for _ in range(N + 1)])

dp[0][0] = Fraction(T)
for r in range(N):
    for c in range(r + 1):
        if dp[r][c] >= Fraction(1):
            dp[r + 1][c + 0] += (dp[r][c] - Fraction(1)) / Fraction(2);
            dp[r + 1][c + 1] += (dp[r][c] - Fraction(1)) / Fraction(2);

cnt = 0
for r in range(N):
    for c in range(r + 1):
        if dp[r][c] >= Fraction(1):
            cnt += 1

print(cnt)

