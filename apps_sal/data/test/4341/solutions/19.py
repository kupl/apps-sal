def rd():
    return list(map(int, input().split()))


(n, m) = rd()
d = {}


def f(x):
    d[x] = d.get(x, 0) + 1


uf = [i for i in range(n)]


def find(i):
    p = uf[i]
    if i == p:
        return p
    else:
        uf[i] = find(p)
        return uf[i]


for _ in range(m):
    (u, v) = sorted(rd())
    u -= 1
    v -= 1
    f(u)
    f(v)
    uf[find(v)] = find(u)
r = [1] * n
for i in range(n):
    r[find(i)] &= d.get(i, 0) == 2
print(sum((i == uf[i] for i in range(n))) + sum(r) - n)
