import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = list(map(int, input().split()))
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    res = k
    que = deque([0])
    visited = [False] * n
    visited[0] = True
    while que:
        v = que.popleft()
        cnt = 0
        for u in edge[v]:
            if not visited[u]:
                visited[u] = True
                cnt += 1
                que.append(u)
        if v == 0:
            for i in range(cnt):
                res *= (k - 1 - i)
                res %= mod
        else:
            for i in range(cnt):
                res *= (k - 2 - i)
                res %= mod
    print(res)


def __starting_point():
    resolve()


__starting_point()
