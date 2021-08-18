n, m, d = map(int, input().split())
ph = [[int(j) for j in input().split()] for i in range(n)]
inf = [[int(j) for j in input().split()] for i in range(m)]
for i in range(n):
    ph[i][1] = -ph[i][1]
for i in range(m):
    inf[i][1] = -inf[i][1]
ph.sort(reverse=True)
inf.sort(reverse=True)
sw, sc = 0, 0
for p in inf:
    sc += p[0]
    d += p[1]
ans = 0
z = m - 1
for p in ph:
    sc += p[0]
    d += p[1]
    while z > 0 and d < 0:
        sc -= inf[z][0]
        d -= inf[z][1]
        z -= 1
    if d >= 0:
        ans = max(ans, sc)
print(ans)
