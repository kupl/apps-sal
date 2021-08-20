(n, a, b, c) = map(int, input().split())
l = [int(input()) for _ in range(n)]


def dfs(i, x, y, z):
    if i == n:
        return abs(a - x) + abs(b - y) + abs(c - z) - 30 if min(x, y, z) > 0 else 10 ** 9
    return min(dfs(i + 1, x, y, z), dfs(i + 1, x + l[i], y, z) + 10, dfs(i + 1, x, y + l[i], z) + 10, dfs(i + 1, x, y, z + l[i]) + 10)


print(dfs(0, 0, 0, 0))
