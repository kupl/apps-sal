(n, k) = map(int, input().split())


def dfs(q, d):
    q = q % 2 ** (d - 1)
    if q == 0:
        print(d)
    else:
        dfs(q, d - 1)


dfs(k, n)
