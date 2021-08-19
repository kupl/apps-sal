from sys import stdin, stdout
from collections import deque


def st():
    return list(stdin.readline().strip())


def li():
    return list(map(int, stdin.readline().split()))


def mp():
    return list(map(int, stdin.readline().split()))


def inp():
    return int(stdin.readline())


def pr(n):
    return stdout.write(str(n) + '\n')


mod = 1000000007
INF = float('inf')


def solve():
    (n, m) = mp()
    d = {i: [] for i in range(n + 1)}
    for i in range(m):
        (a, b) = mp()
        d[a].append(b)
        d[b].append(a)
    (x, y) = mp()
    v = [False for i in range(n + 1)]
    q = deque()
    q.append(x)
    dis = [INF for i in range(n + 1)]
    dis[x] = 0
    v[x] = True
    while q:
        a = q.popleft()
        for i in d[a]:
            if not v[i]:
                v[i] = True
                q.append(i)
                dis[i] = dis[a] + 1
    if not v[y]:
        pr(0)
    else:
        pr(dis[y])


for _ in range(1):
    solve()
