import sys
n, m = list(map(int, input().split()))
s = [input() for i in range(n)]
dp = [[-1 for i in range(m)] for j in range(n)]
ans = []
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if (s[i][j] == '*' and s[i + 1][j] == '*' and s[i - 1][j] == '*' and s[i][j - 1] == '*' and s[i][j + 1] == '*'):
            x = 0
            while i - x > -1 and x + i < n and j - x > -1 and x + j < m and s[i + x][j] == '*' and s[i - x][j] == '*' and s[i][j - x] == '*' and s[i][j + x] == '*':
                dp[i + x][j], dp[i - x][j], dp[i][j - x], dp[i][j + x] = 1, 1, 1, 1
                x += 1
            if x != 1:
                ans.append([i + 1, j + 1, x - 1])
            else:
                dp[i][j] = -1
for i in range(n):
    for j in range(m):
        if s[i][j] == '*' and dp[i][j] == -1:
            print(-1)
            return
print(len(ans))
for i in ans:
    print(*i)
