I = lambda: map(int, input().split())
n, m, k = I()
f = [['.' for _ in range(m)] for _ in range(n)]
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] != '.':
            f[i][j] = s[j]
ans = [0] * m
for i in range(n):
    for j in range(m):
        if j - i >= 0 and f[i][j - i] == 'R':
            ans[j] += 1
        if j + i < m and f[i][j + i] == 'L':
            ans[j] += 1
        if f[0][j] == 'D':
            ans[j] += 1
        if i + i < n and f[i + i][j] == 'U':
            ans[j] += 1
print(*ans)
