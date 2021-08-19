(n, m) = map(int, input().split())
a = [input() for i in range(n)]
(x1, y1, x2, y2) = (100000, 100000, -1, -1)
for i in range(n):
    for j in range(m):
        if a[i][j] == 'X':
            (x1, y1) = (min(j, x1), min(i, y1))
            (x2, y2) = (max(j, x2), max(i, y2))
f = True
for i in range(y1, y2 + 1):
    for j in range(x1, x2 + 1):
        if a[i][j] != 'X':
            f = False
if not f or ((x2 - x2) % m and (y2 - y1) % n):
    print('NO')
else:
    print('YES')
