import sys
from functools import reduce

MAX_INT = 2**62 - 1
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

MOD = 10**9 + 7


def mul_mod(*args, mod=MOD):
    return reduce(lambda a, b: a * b % mod, args)


def solve(g, f, fi, m):
    mul = mul_mod

    stack = [(0, 1)]
    pre_order = []
    n = len(g) - 1

    while stack:
        pre, cur = stack.pop()
        pre_order.append((pre, cur))

        for nxt in g[cur]:
            if nxt == pre:
                continue
            stack.append((cur, nxt))

    size = [1] * (n + 1)
    dp = [1] * (n + 1)

    for pre, cur in reversed(pre_order):
        dp[cur] = mul(dp[cur], f[size[cur] - 1])
        dp[pre] = mul(dp[pre], dp[cur], fi[size[cur]])
        size[pre] += size[cur]

    ans = [1] * (n + 1)
    ans[1] = dp[1]

    for pre, cur in pre_order[1:]:
        i = size[cur]
        temp = mul(ans[pre], f[n - i - 1], fi[n - 1], f[i], pow(dp[cur], m - 2, m))
        ans[cur] = mul(f[n - 1], temp, fi[n - i], dp[cur], fi[i - 1])
    print(*ans[1:], sep='\n')


def main():
    mul = mul_mod
    mod = MOD
    n = int(input())
    g = [[] for _ in range(n + 1)]

    fact = [1] * (n + 1)
    fact_inv = [0] * (n + 1)

    for i in range(1, n + 1):
        fact[i] = mul(fact[i - 1], i)

    fact_inv[-1] = pow(fact[-1], mod - 2, mod)

    for i in range(n)[::-1]:
        fact_inv[i] = mul(fact_inv[i + 1], (i + 1))

    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    solve(g, fact, fact_inv, mod)


def __starting_point():

    main()


__starting_point()
