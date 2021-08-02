from typing import List, Tuple


def main():
    n, m = list(map(int, input().split()))
    g = []
    for _ in range(m):
        a, b = list(map(int, input().split()))
        g.append((a, b))
    print((osp(n, g)))


def osp(n: int, g: List[Tuple[int, int]]) -> int:
    v = [False] * n

    return dfs(0, v, n, g)


def dfs(i, v, n, g):
    v[i] = True
    if all(v):
        v[i] = False
        return 1

    cnt = 0
    for j in range(n):
        if v[j]:
            continue
        if not ((i + 1, j + 1) in g or (j + 1, i + 1) in g):
            continue
        cnt += dfs(j, v, n, g)

    v[i] = False
    return cnt


def __starting_point():
    main()


__starting_point()
