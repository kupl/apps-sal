from collections import Counter
(n, m, k) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
(v, l) = ([0] * n, [False] * k)
for j in range(m):
    c = Counter((a[i][j] for i in range(n)))
    for i in range(n):
        if not v[i] and a[i][j] and (l[a[i][j] - 1] or c[a[i][j]] > 1):
            v[i] = j + 1
            l[a[i][j] - 1] = True
            a[i] = [0] * m
print(*v, sep='\n')
