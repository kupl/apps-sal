(n, m) = map(int, input().split())
d = [0] * m
K = [[] for i in range(n)]
for i in range(m):
    (p, y) = map(int, input().split())
    K[p - 1].append((i, y))
for i in range(n):
    K[i].sort(key=lambda x: x[1])
    c = 1
    for (a, b) in K[i]:
        ken = str(i + 1)
        t = str(c)
        d[a] = str('0' * (6 - len(ken))) + ken + str('0' * (6 - len(t))) + t
        c += 1
for i in d:
    print(i)
