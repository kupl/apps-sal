def f(): return map(int, input().split())


n, m = f()
p = list(range(n))


def g(i):
    while i != p[i]:
        i = p[i]
    return i


q = 'yes' if m == n - 1 else 'no'

for j in range(m):
    a, b = f()
    u, v = g(a - 1), g(b - 1)
    if u == v:
        q = 'no'
    p[u] = v

print(q)
