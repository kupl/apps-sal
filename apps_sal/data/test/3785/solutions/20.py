n, m, k = map(int, input().split())
g = [input().replace('.', 'X') for i in range(n)]
k = n * m - k - sum(i.count('
g=[list(i) for i in g]
i, p=0, []
while k:
    if 'X' in g[i]:
        j=g[i].index('X')
        g[i][j], p='.', [(i, j)]
        k -= 1
        break
    i += 1
while k:
    x, y=p.pop()
    for i, j in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
        if i < 0 or j < 0:
            continue
        if i < n and j < m and g[i][j] == 'X':
            g[i][j]='.'
            p.append((i, j))
            k -= 1
            if k == 0:
                break
for i in range(n):
    g[i]=''.join(g[i])
print('\n'.join(g))
