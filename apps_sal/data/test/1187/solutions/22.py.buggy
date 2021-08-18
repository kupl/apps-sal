vis = []
ans = []
nodes = []


def dfs(A):
    nonlocal vis, ans, nodes
    vis[A] = 1
    for (B, index) in nodes[A]:
        if ans[index] != 0:
            continue
        if vis[B] == 1:
            ans[index] = 2
        else:
            ans[index] = 1
            dfs(B)

    vis[A] = 2


def main():
    nonlocal vis, ans, nodes
    n, m = map(int, input().strip().split())
    vis = [-1] * (n + 10)
    ans = [0] * (m + 10)
    nodes = [[] for i in range(n + 10)]
    for i in range(m):
        a, b = map(int, input().strip().split())
        nodes[a].append((b, i))
    for i in range(1, n + 1):
        if vis[i] == -1:
            dfs(i)
    if 2 in ans:
        print(2)
    else:
        print(1)
    for i in range(m):
        print(ans[i])


def __starting_point():
    main()


__starting_point()
