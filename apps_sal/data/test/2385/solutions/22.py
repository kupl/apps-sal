def main():
    from sys import stdin
    input = stdin.readline
    n = int(input())
    ab = [list(map(int, input().split())) for _ in [0] * (n - 1)]
    g = [set() for _ in [0] * n]
    for (a, b) in ab:
        g[a - 1].add(b - 1)
        g[b - 1].add(a - 1)
    mod = 10 ** 9 + 7
    fact = [1, 1]
    inv = [pow(i, mod - 2, mod) for i in range(n + 1)]
    for i in range(2, n + 1):
        fact.append(fact[-1] * i % mod)

    class rerooting:

        def __init__(self, tree, ini):

            def merge(a, b):
                return a * b % mod

            def adj_bu(a, i):
                return a * inv[size[i]] % mod

            def adj_td(a, i, p):
                return a * inv[n - size[i]] % mod

            def adj_fin(a, i):
                return a * fact[n - 1] % mod
            T = g
            P = [-1] * n
            q = [0]
            order = []
            while q:
                i = q.pop()
                order.append(i)
                for a in T[i]:
                    if a != P[i]:
                        P[a] = i
                        T[a].remove(i)
                        q.append(a)
            T = [list(i) for i in T]
            size = [1] * n
            for i in order[1:][::-1]:
                size[P[i]] += size[i]
            ME = [ini] * n
            DP = [0] * n
            for i in order[1:][::-1]:
                DP[i] = adj_bu(ME[i], i)
                p = P[i]
                ME[p] = merge(ME[p], DP[i])
            DP[order[0]] = adj_fin(ME[order[0]], order[0])
            TD = [ini] * n
            for i in order:
                ac = TD[i]
                for j in T[i]:
                    TD[j] = ac
                    ac = merge(ac, DP[j])
                ac = ini
                for j in T[i][::-1]:
                    TD[j] = adj_td(merge(TD[j], ac), j, i)
                    ac = merge(ac, DP[j])
                    DP[j] = adj_fin(merge(ME[j], TD[j]), j)
            for i in DP:
                print(i)
    rerooting(g, 1)


main()
