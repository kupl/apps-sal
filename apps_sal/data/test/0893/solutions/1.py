f = lambda: map(int, input().split())
m = 1000000007

d, n = f()
t = list(f())
p = [[] for i in range(n)]
for j in range(n - 1):
    u, v = f()
    p[u - 1].append(v - 1)
    p[v - 1].append(u - 1)


def g(u, x, y):
    s = 1
    for v in p[u]:
        if 0 < t[v] - t[y] <= d or t[v] == t[y] and v > y:
            if v != x: s += s * g(v, u, y) % m
    return s


print(sum(g(y, -1, y) for y in range(n)) % m)
