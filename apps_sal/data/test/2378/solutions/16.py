import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def solve():
    N = int(input())
    AB = [tuple(map(int, input().split())) for i in range(N - 1)]
    MOD = 10**9 + 7
    es = [[] for _ in range(N)]
    for a, b in AB:
        a, b = a - 1, b - 1
        es[a].append(b)
        es[b].append(a)

    cs = [1] * N

    def dfs(v, p=-1):
        ret = 1
        for to in es[v]:
            if to == p:
                continue
            ret += dfs(to, v)
        cs[v] = ret
        return ret
    dfs(0)

    pow2 = [1]
    for i in range(N):
        pow2.append((pow2[-1] * 2) % MOD)

    ans = 0
    for i in range(N):
        if len(es[i]) == 1:
            continue
        ans += pow2[N - 1] - 1
        c = 0
        for to in es[i]:
            if cs[to] > cs[i]:
                continue
            c += cs[to]
            ans -= pow2[cs[to]] - 1
        ans -= pow2[N - c - 1] - 1

    ans *= pow(pow2[N], MOD - 2, MOD)
    print(ans % MOD)


solve()
