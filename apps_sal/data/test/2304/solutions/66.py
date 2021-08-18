from sys import stdin
from collections import deque


def main():
    readline = stdin.readline
    n, m = map(int, readline().split())
    G = [[] for _ in range(n + 1)]
    for i in range(m):
        l, r, d = map(int, readline().split())
        G[l].append((r, d))
        G[r].append((l, -d))

    flags = [False] * (n + 1)
    flags[0] = True
    inf = 10**10
    x = [-inf] * (n + 1)
    q = deque([])
    ans = True
    for i in range(1, n + 1):
        if ans == False:
            break
        if flags[i] == False:
            x[i] = 0
            flags[i] = True
            q.append(i)
            while len(q) > 0:
                now = q.popleft()
                for t in G[now]:
                    nex = t[0]
                    cost = t[1]
                    if x[nex] == -inf:
                        x[nex] = x[now] + cost
                    else:
                        if x[nex] != x[now] + cost:
                            ans = False
                            break
                    if flags[nex] == False:
                        flags[nex] = True
                        q.append(nex)

    print("Yes" if ans else "No")


def __starting_point():
    main()


__starting_point()
