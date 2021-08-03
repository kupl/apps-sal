n, a, b, c, *l = map(int, open(0).read().split())


def dfs(x, y, z, r):
    if r == n:
        return abs(a - x) + abs(b - y) + abs(c - z) - 30 if min(x, y, z) > 0 else 10**9
    return min(
        dfs(x + l[r], y, z, r + 1) + 10,
        dfs(x, y + l[r], z, r + 1) + 10,
        dfs(x, y, z + l[r], r + 1) + 10,
        dfs(x, y, z, r + 1)
    )


print(dfs(0, 0, 0, 0))
