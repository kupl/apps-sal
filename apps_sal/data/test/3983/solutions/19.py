from collections import Counter
t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    *p, = list(range(n))
    r = [0] * n

    def par(x):
        if p[x] == x:
            return x
        res = p[x] = par(p[x])
        return res

    def union(x, y):
        px = par(x)
        py = par(y)
        if px == py:
            return
        if r[px] > r[py]:
            p[py] = px
            r[py] += 1
        elif r[px] < r[py]:
            p[px] = py
            r[px] += 1
        else:
            p[px] = py
            r[py] += 1

    for _ in range(m):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        union(u, v)
    if n % 2:
        print(('First' if (n * (n - 1) // 2 - m) % 2 else 'Second'))
        continue

    for i in range(n):
        par(i)
    cp = Counter(p)
    if (cp[par(0)] - cp[par(n - 1)]) % 2:  # par
        print('First')
        continue
    if (n * (n - 1) // 2 - cp[par(0)] * cp[par(n - 1)] - m) % 2:
        print('First')
    else:
        print('Second')
