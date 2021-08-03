import sys
sys.setrecursionlimit(10 ** 6)


def LI(): return list(map(int, input().split()))


N = int(input())
AB = [LI() for _ in range(N - 1)]

link = [[] for _ in range(N)]
children = [[] for _ in range(N)]
w = [1] * N
visit = [False] * N

MOD = 10 ** 9 + 7


def create_link():
    for a, b in AB:
        link[a - 1].append(b - 1)
        link[b - 1].append(a - 1)


def dfs(s):
    visit[s] = True
    for t in link[s]:
        if visit[t]:
            continue
        children[s].append(t)
        dfs(t)
        w[s] += w[t]


def modinv(x):
    return pow(x, MOD - 2, MOD)


def main():
    create_link()
    dfs(0)
    p2 = [None] * (N + 1)
    p2[0] = 1
    for i in range(N):
        p2[i + 1] = 2 * p2[i] % MOD

    x = 0
    for i in range(N):
        s = p2[N - w[i]]
        for j in children[i]:
            s = (s + p2[w[j]] - 1) % MOD
        x = (x + p2[N - 1] - s) % MOD
    y = p2[N]

    ans = x * modinv(y) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
