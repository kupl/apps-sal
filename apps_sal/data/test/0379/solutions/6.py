n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(input())

inf = 10 ** 9
p, q = inf, inf
r, s = -1, -1

for i in range(n):
    for j in range(m):
        if a[i][j] == 'X':
            p = min(p, i)
            q = min(q, j)
            r = max(r, i)
            s = max(s, j)

ok = True
for i in range(n):
    for j in range(m):
        if a[i][j] == 'X':
            ok &= p <= i <= r and q <= j <= s
        if a[i][j] == '.':
            ok &= not (p <= i <= r and q <= j <= s)

if ok:
    print('YES')
if not ok:
    print('NO')

