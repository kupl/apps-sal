def read(): return map(int, input().split())


n, m = read()
a = [input() for i in range(n)]
c1 = '1234567890'
c2 = 'qwertyuiopasdfghjklzxcvbnm'
c3 = '#&*'
inf = 10 ** 20
l1 = [inf] * n
l2 = [inf] * n
l3 = [inf] * n
for i in range(n):
    for j in range(m):
        if a[i][j] in c1:
            l1[i] = min(l1[i], j, m - j)
        if a[i][j] in c2:
            l2[i] = min(l2[i], j, m - j)
        if a[i][j] in c3:
            l3[i] = min(l3[i], j, m - j)
ans = inf
for i in range(n):
    for j in range(n):
        for k in range(n):
            if len({i, j, k}) < 3:
                continue
            cur = l1[i] + l2[j] + l3[k]
            ans = min(ans, cur)
print(ans)
