from collections import deque
import sys
input = sys.stdin.readline
mod = 998244353
t = int(input())


def isbip2(i, vis, col, f):
    q = deque()
    q.append(i)
    vis[i] = 1
    col[i] = 0
    f[0] += 1
    while len(q) > 0:
        z = q.popleft()
        for j in a[z]:
            if col[z] == col[j]:
                return 0
            if vis[j] == 0:
                vis[j] = 1
                col[j] = col[z] ^ 1
                f[col[j]] += 1
                q.append(j)
    return 1


def isbip(col, vis, n):
    c = 1
    z = 0
    o = 0
    f = [0, 0]
    for i in range(1, n + 1):
        if vis[i]:
            continue
        if not isbip2(i, vis, col, f):
            return 0
        c = c % mod * (pow(2, f[0] - z, mod) + pow(2, f[1] - o, mod)) % mod
        z = f[0]
        o = f[1]
    return c


while t > 0:
    t -= 1
    (n, m) = list(map(int, input().split()))
    col = [-1 for i in range(n + 1)]
    a = [[] for i in range(n + 1)]
    vis = [0 for i in range(n + 1)]
    for i in range(m):
        (x, y) = list(map(int, input().split()))
        a[x].append(y)
        a[y].append(x)
    print(isbip(col, vis, n))
