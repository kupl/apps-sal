
import sys
sys.setrecursionlimit(10 ** 6)


def main2():
    n, q = list(map(int, input().split()))
    tree = [[] for i in range(n)]
    point = [0] * n

    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        tree[b - 1].append(a - 1)
        tree[a - 1].append(b - 1)
    for i in range(q):
        p, x = list(map(int, input().split()))
        point[p - 1] += x

    def dfs(v, parent):
        nonlocal point, tree
        for next_val in tree[v]:
            if next_val == parent:
                continue
            point[next_val] += point[v]
            dfs(next_val, v)
    dfs(0, 0)
    print((*point))


def __starting_point():
    main2()


__starting_point()
