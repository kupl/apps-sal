import sys
sys.setrecursionlimit(10 ** 7)

MOD = 998244353


def init(G, robots, fs, p):
    q = p
    while q < len(robots) and robots[q][0] < robots[p][0] + robots[p][1]:
        if fs[q]:
            G[p].append(q)
            fs[q] = False
            q = init(G, robots, fs, q) - 1
        q += 1
    return q


def calc(G, p, fs):
    fs[p] = False
    if len(G[p]) == 0:
        return 2
    tmp = 1
    for v in G[p]:
        tmp *= calc(G, v, fs)
        tmp %= MOD
    tmp += 1
    return tmp


def main():
    n = int(input())
    robots = [list(map(int, input().split())) for _ in range(n)]
    G = [[] for _ in range(n)]
    robots.sort(key=lambda x: x[0])
    fs = [True] * n
    q = 0
    while q < n:
        if fs[q]:
            fs[q] = False
            init(G, robots, fs, q)
        else:
            q += 1
    fs = [True] * n
    ans = 1
    for i in range(n):
        if fs[i]:
            ans *= calc(G, i, fs)
            ans %= MOD
    print(ans % MOD)


def __starting_point():
    main()


__starting_point()
