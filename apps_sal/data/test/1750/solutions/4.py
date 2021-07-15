from sys import stdin
from collections import deque


def main():
    n = int(input()) + 1
    g = [[] for _ in range(n)]
    for s in range(n-2):
        u, v = list(map(int, input().split()))
        g[u].append(v)
        g[v].append(u)
    cc, palette, q = [0] * n, [True] * n, deque(((1, 0, 1),))
    cc[1] = 1
    while q:
        u, a, b = q.popleft()
        
        c = 1
        for v in g[u]:
            if not cc[v]:
                while c in [a,b]:
                    c += 1
                cc[v] = c
                q.append((v, b, c))
                c += 1
        
    print(max(cc))
    print(' '.join(map(str, cc[1:])))


def __starting_point():
    main()
        

__starting_point()
