n, m = list(map(int, input().split()))
g = [input() for _ in range(n)]
r, c = set(), set()
for i in range(n):
    for j in range(m):
        if g[i][j] == 'X':
            r.add(i)
            c.add(j)
g = g[min(r):max(r) + 1]
g = list([x[min(c): max(c) + 1] for x in g])

good = True
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j] != 'X':
            good = False
            break
print('YES' if good else 'NO')
