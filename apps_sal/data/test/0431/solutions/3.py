(n, m) = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
l = 0
r = INF = 100000
h = 0
while h < n:
    if a[h] == '0' * (m + 2):
        h += 1
    else:
        break
if h != n:
    for i in range(n - 1, h, -1):
        x = INF
        y = 0
        for j in range(m + 2):
            if a[i][j] == '1':
                x = min(x, j)
                y = max(y, j)
        if x != INF:
            ll = min(l + y * 2, r + m + 1)
            rr = min(l + m + 1, r + (m + 1 - x) * 2)
            l = ll
            r = rr
    x = INF
    y = 0
    for j in range(m + 2):
        if a[h][j] == '1':
            x = min(x, j)
            y = max(y, j)
    ans = min(l + y, r + (m + 1 - x))
    print(ans + n - 1 - h)
else:
    print(0)
