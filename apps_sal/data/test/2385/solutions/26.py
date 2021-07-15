def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline

    ## comb
    mod = 1000000007

    def make_fact(n):
        fact = [1]*(n+1)
        ifact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i % mod
        ifact[n] = pow(fact[n], mod-2, mod)
        for i in range(n, 0, -1):
            ifact[i-1] = ifact[i]*i % mod
        return fact, ifact
    fact, ifact = make_fact(2000002)

    def comb(n, k):
        if k < 0 or k > n: return 0
        return fact[n]*ifact[k]*ifact[n-k] % mod

    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N-1)]
    graph = [[] for _ in range(N + 1)]
    for a, b in AB:
        graph[a].append(b)
        graph[b].append(a)

    # dfs
    root = 1
    parent = [0] * (N + 1)
    order = []
    stack = [root]
    while stack:
        x = stack.pop()
        order.append(x)
        for y in graph[x]:
            if y == parent[x]:
                continue
            parent[y] = x
            stack.append(y)

    # 方向ごと？
    size_d = [0] * (N + 1)
    dp_d = [1] * (N + 1)

    for v in order[::-1]:
        dp_d[v] *= fact[size_d[v]]
        dp_d[v] %= mod
        p = parent[v]
        s = size_d[v] + 1
        size_d[p] += s
        dp_d[p] *= ifact[s] * dp_d[v]
        dp_d[p] %= mod

    size_u = [N - 2 - x for x in size_d]
    dp_u = [1] * (N + 1)

    for v in order[1:]:
        p = parent[v]
        x = dp_d[p]
        x *= dp_u[p]
        x *= ifact[size_d[p]]
        x *= fact[size_d[v] + 1]
        x *= pow(dp_d[v], mod - 2, mod)
        x *= fact[size_u[v]]
        x *= ifact[size_u[p] + 1]
        dp_u[v] = x % mod

    for xd, xu, sd, su in zip(dp_d[1:], dp_u[1:], size_d[1:], size_u[1:]):
        su += 1
        x = xd * xu * comb(sd+su, su) % mod
        print(x)

main()


