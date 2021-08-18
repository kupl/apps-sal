from sys import stdin
from collections import deque


def main():
    readline = stdin.readline
    n, m = map(int, readline().split())
    G = [[] for _ in range(n * 3)]
    for i in range(m):
        a, b = map(lambda x: int(x) - 1, readline().split())
        for j in range(3):
            G[3 * a + j].append(3 * b + (j + 1) % 3)

    s, t = map(lambda x: int(x) - 1, readline().split())
    s *= 3
    t *= 3
    d = deque([s])
    flags = [-1] * (3 * n)
    flags[s] = 0
    while len(d) > 0:
        now = d.popleft()
        for nex in G[now]:
            if flags[nex] == -1:
                flags[nex] = flags[now] + 1
                d.append(nex)

    print(flags[t] // 3)


def __starting_point():
    main()


__starting_point()
