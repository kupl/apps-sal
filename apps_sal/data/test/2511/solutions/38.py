from sys import stdin
from collections import deque


def main():
    readline = stdin.readline
    mod = 10 ** 9 + 7
    (n, k) = map(int, readline().split())
    G = [[] for _ in range(n)]
    for i in range(n - 1):
        (a, b) = map(lambda x: int(x) - 1, readline().split())
        G[a].append(b)
        G[b].append(a)
    ans = k
    stack = deque([0])
    flags = [False] * n
    flags[0] = True
    while len(stack) > 0:
        now = stack.pop()
        if now == 0:
            ans *= P(k - 1, len(G[0]), mod)
            ans %= mod
        else:
            ans *= P(k - 2, len(G[now]) - 1, mod)
            ans %= mod
        for nex in G[now]:
            if flags[nex] == False:
                flags[nex] = True
                stack.append(nex)
    print(ans)


def P(n, k, mod):
    res = 1
    for m in range(n, n - k, -1):
        res *= m
        res %= mod
    return res


def __starting_point():
    main()


__starting_point()
