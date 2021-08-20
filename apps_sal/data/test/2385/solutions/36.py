import sys
from collections import deque
sys.setrecursionlimit(1000000)


def comb(n, r, fact, revfact, mod):
    return fact[n] * (revfact[n - r] * revfact[r]) % mod % mod


def dfs(i, parent, DP, sNum, E, fact, revfact, mod):
    Ans = 1
    sonNode = 1
    S = []
    for e in E[i]:
        if e != parent:
            (mult, sn) = dfs(e, i, DP, sNum, E, fact, revfact, mod)
            S.append(sn)
            Ans *= mult
            Ans %= mod
            sonNode += sn
    stotal = sonNode - 1
    for s in S:
        Ans *= comb(stotal, s, fact, revfact, mod)
        Ans %= mod
        stotal -= s
    DP[i] = Ans
    sNum[i] = sonNode - 1
    return (Ans, sonNode)


def solve():
    input = sys.stdin.readline
    N = int(input())
    E = [[] for _ in range(N)]
    for _ in range(N - 1):
        (a, b) = list(map(int, input().split()))
        E[a - 1].append(b - 1)
        E[b - 1].append(a - 1)
    mod = 7 + 10 ** 9
    fact = [1] * (N + 1)
    for i in range(N):
        fact[i + 1] = (i + 1) * fact[i] % mod
    revfact = [1] * (N + 1)
    revfact[N] = pow(fact[N], mod - 2, mod)
    for i in reversed(list(range(N))):
        revfact[i] = (i + 1) * revfact[i + 1] % mod
    DP = [1] * N
    sNum = [0] * N
    usNum = [0] * N
    dfs(0, 0, DP, sNum, E, fact, revfact, mod)
    q = deque()
    for e in E[0]:
        q.append((e, 0))
    while q:
        (nn, parn) = q.popleft()
        upperMult = DP[parn] * pow(comb(N - 1, sNum[nn] + 1, fact, revfact, mod), mod - 2, mod)
        usNum[nn] = upperNum = sNum[parn] - sNum[nn] + usNum[parn]
        DP[nn] = upperMult * comb(N - 1, upperNum, fact, revfact, mod) % mod
        for e in E[nn]:
            if e != parn:
                q.append((e, nn))
    print('\n'.join(map(str, DP)))
    return 0


def __starting_point():
    solve()


__starting_point()
