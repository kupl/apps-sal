from heapq import *
n, m, r, k = map(int, input().split())
u, v = n // 2, m // 2
h = []
def g(z, l): return min(z + 1, l - z, l - r + 1, r)


def f(x, y):
    if 0 <= x < n and 0 <= y < m:
        s = g(x, n) * g(y, m)
        heappush(h, (-s, x, y))


f(u, v)
t = 0
for i in range(k):
    s, x, y = heappop(h)
    t -= s
    if x <= u:
        f(x - 1, y)
    if x == u and y <= v:
        f(x, y - 1)
    if x >= u:
        f(x + 1, y)
    if x == u and y >= v:
        f(x, y + 1)
print(t / (n - r + 1) / (m - r + 1))
