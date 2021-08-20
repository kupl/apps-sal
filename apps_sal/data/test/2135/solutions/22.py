line = input().split()
(h, w) = (int(line[0]), int(line[1]))
grid = []
for i in range(0, h):
    line = input()
    grid.append(line)
q = int(input().split()[0])
dp = [[[0 for z in range(0, 2)] for x in range(w)] for y in range(h)]
for i in range(0, h):
    for j in range(0, w):
        dp[i][j][0] += (dp[i - 1][j][0] if i > 0 else 0) + (dp[i][j - 1][0] if j > 0 else 0) - (dp[i - 1][j - 1][0] if i > 0 and j > 0 else 0)
        dp[i][j][1] += (dp[i - 1][j][1] if i > 0 else 0) + (dp[i][j - 1][1] if j > 0 else 0) - (dp[i - 1][j - 1][1] if i > 0 and j > 0 else 0)
        dp[i][j][0] += 1 if i > 0 and grid[i][j] == '.' and (grid[i - 1][j] == '.') else 0
        dp[i][j][1] += 1 if j > 0 and grid[i][j] == '.' and (grid[i][j - 1] == '.') else 0
while q > 0:
    line = input().split()
    (r1, c1, r2, c2) = (int(line[0]), int(line[1]), int(line[2]), int(line[3]))
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    ans = 0
    ans += dp[r2][c2][0] + dp[r2][c2][1]
    ans -= dp[r1 - 1][c2][0] + dp[r1 - 1][c2][1] if r1 > 0 else 0
    ans -= dp[r2][c1 - 1][0] + dp[r2][c1 - 1][1] if c1 > 0 else 0
    ans += dp[r1 - 1][c1 - 1][0] + dp[r1 - 1][c1 - 1][1] if r1 > 0 and c1 > 0 else 0
    ans -= dp[r1][c2][0] - (dp[r1 - 1][c2][0] if r1 > 0 else 0) - (dp[r1][c1 - 1][0] if c1 > 0 else 0) + (dp[r1 - 1][c1 - 1][0] if c1 > 0 and r1 > 0 else 0)
    ans -= dp[r2][c1][1] - (dp[r2][c1 - 1][1] if c1 > 0 else 0) - (dp[r1 - 1][c1][1] if r1 > 0 else 0) + (dp[r1 - 1][c1 - 1][1] if c1 > 0 and r1 > 0 else 0)
    print(ans)
    q -= 1
