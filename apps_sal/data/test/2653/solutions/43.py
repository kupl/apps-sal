def solve():
    import sys
    sys.setrecursionlimit(10**6)

    def dfs(tree, n, ans):
        for i in tree[n]:
            ans[i] += ans[n]
            tree[i].remove(n)
            dfs(tree, i, ans)

    n, q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n - 1)]
    px = [list(map(int, input().split())) for _ in range(q)]

    g = [[] for _ in range(n)]
    for i in range(n - 1):
        g[ab[i][0] - 1].append(ab[i][1] - 1)
        g[ab[i][1] - 1].append(ab[i][0] - 1)

    ans = [0] * n
    for i in range(q):
        ans[px[i - 1][0] - 1] += px[i - 1][1]
    dfs(g, 0, ans)

    print(*ans)


def __starting_point():
    solve()


__starting_point()
