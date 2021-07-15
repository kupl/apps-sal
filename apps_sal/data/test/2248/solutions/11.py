f = lambda: map(int, input().split())
 
n, m = f()
p = [[] for i in range(n)]
for j in range(m):
    a, b = f()
    p[a - 1].append(b - 1)
    p[b - 1].append(a - 1)
 
def g(i):
    u, t = [1] * n, (0, i)
    s = [t]
    while s:
        d, i = s.pop()
        u[i] = 0
        if d > t[0]: t = (d, i)
        s += [(d + 1, j) for j in p[i] if u[j]]
    return t
 
print(g(g(0)[1])[0])
