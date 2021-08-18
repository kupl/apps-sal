n, k = list(map(int, input().split()))
f = [list(input()) for _ in range(n)]

ans = (1, 1)
r = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if f[i][j] == '
        r[i][j] = 0
        elif i == 0:
            r[i][j] = 1
        else:
            r[i][j] = r[i - 1][j] + 1
c = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if f[i][j] == '
        c[i][j] = 0
        elif j == 0:
            c[i][j] = 1
        else:
            c[i][j] = c[i][j - 1] + 1

s = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for l in range(k):
            if i + l < n and k <= r[i + l][j]:
                s[i][j] += 1
            if j + l < n and k <= c[i][j + l]:
                s[i][j] += 1
        if s[ans[0] - 1][ans[1] - 1] < s[i][j]:
            ans = (i + 1, j + 1)
print(' '.join(map(str, ans)))
