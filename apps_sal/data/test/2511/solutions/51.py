from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, K = map(int, input().split())
    to = [[] for _ in range(N)]
    MOD = 10**9 + 7
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)

    MAX_N = 3 * 10 ** 5
    MOD = 10 ** 9 + 7
    fac = [0] * MAX_N
    inv = [0] * MAX_N
    finv = [0] * MAX_N
    fac[0] = 1; fac[1] = 1
    inv[1] = 1
    finv[0] = 1; finv[1] = 1

    def com_init():
        for i in range(2, MAX_N):
            fac[i] = fac[i - 1] * i % MOD
            inv[i] = -(MOD // i) * inv[MOD % i] % MOD
            finv[i] = finv[i - 1] * inv[i] % MOD

    def perm(n, r):
        if n < 0: return 0
        elif r > n: return 0

        return fac[n] * finv[n - r] % MOD

    # dfs
    com_init()

    def dfs(s):
        stack = deque()
        stack.append((s, -1))  # now, par
        res = K
        while stack:
            now, par = stack.pop()

            if now == 0:
                children = len(to[now])
            else:
                children = len(to[now]) - 1

            if now == 0:
                nx_col = K - 1
            else:
                nx_col = K - 2

            res *= perm(nx_col, children)
            res %= MOD

            if children == 0 and now != 0:
                continue

            for nv in to[now]:
                if nv != par:
                    stack.append((nv, now))
        return res
    ans = dfs(0)
    print(ans)


def __starting_point():
    main()


__starting_point()
