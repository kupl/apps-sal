from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


def main():
    n = ii()
    edge = [[] for _ in range(n)]
    ans = [0] * (n - 1)
    for i in range(n - 1):
        (u, v) = mi()
        u -= 1
        v -= 1
        edge[u].append((v, i))
        edge[v].append((u, i))
    k = 0
    q = deque([0])
    visited = [False] * n
    visited[0] = True
    c = [0] * n
    while q:
        v = q.popleft()
        cur = 1
        k = max(k, len(edge[v]))
        for (nv, idx) in edge[v]:
            if visited[nv]:
                continue
            if cur == c[v]:
                cur += 1
            visited[nv] = True
            c[nv] = cur
            ans[idx] = cur
            cur += 1
            q.append(nv)
    print(k)
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
