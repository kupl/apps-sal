(n, m) = list(map(int, input().split()))
L = [input() for _ in range(n)]
C = [[0 for _ in range(m)] for _ in range(n)]
(x1, y1) = (500, 500)
(x2, y2) = (-1, -1)
for i in range(n):
    sa = 0
    for j in range(m):
        if L[i][j] == 'B':
            x1 = min(i, x1)
            x2 = max(i, x2)
            y1 = min(j, y1)
            y2 = max(j, y2)
            sa += 1
        if i > 0:
            C[i][j] += C[i - 1][j]
        C[i][j] += sa
if x2 == -1:
    print(1)
else:
    a = max(x2 - x1, y2 - y1)
    ans = 1000000
    for i in range(n):
        for j in range(m):
            if i + a < n and j + a < m and (i <= x1) and (x2 <= i + a) and (j <= y1) and (y2 <= j + a):
                s = C[i + a][j + a]
                if i > 0:
                    s -= C[i - 1][j]
                if j > 0:
                    s -= C[i][j - 1]
                if i > 0 and j > 0:
                    s -= C[i - 1][j - 1]
                ans = min((a + 1) * (a + 1) - s, ans)
    if ans == 1000000:
        ans = -1
    print(ans)
