def main():
    n = int(input())
    xd = [list(map(int, input().split())) for _ in range(n)]
    mod = 998244353
    INF = 10 ** 10

    xx = [(x, x + d, i) for i, (x, d) in enumerate(xd, 1)]
    xx.sort()
    c = [[] for _ in range(n + 1)]
    stack = [(INF, 0)]
    for l, r, i in xx:
        while stack[-1][0] <= l:
            stack.pop()

        ip = stack[-1][1]
        c[ip].append(i)
        stack.append((r, i))

    dp = [1] * (n + 1)
    for _, _, u in xx[::-1]:
        for v in c[u]:
            dp[u] *= dp[v]
            dp[u] %= mod

        dp[u] += 1
        dp[u] %= mod

    for v in c[0]:
        dp[0] *= dp[v]
        dp[0] %= mod

    ans = dp[0]
    print(ans)


def __starting_point():
    main()

__starting_point()
