from sys import setrecursionlimit
setrecursionlimit(int(1e9))
def intput(): return [int(i) for i in input().split()]


# Write your code here
n, m, k = intput()
blasters = [intput() for i in range(k)]
grid = [[1] * n for i in range(m)]

for bx, by, t, f in blasters:
    bx -= 1
    by -= 1

    for x in range(n):
        k = x + by - abs(bx - x) - t
        if k >= 0 and k % f == 0:
            grid[by][x] = 0

    for y in range(m):
        k = bx + y - abs(by - y) - t
        if k >= 0 and k % f == 0:
            grid[y][bx] = 0


def solve(x, y):
    if not grid[y][x]:
        return 0
    if x == n - 1 and y == m - 1:
        return 1
    res = 0
    if x != n - 1:
        res = solve(x + 1, y)
    if y != m - 1:
        res = res or solve(x, y + 1)
    return res


if solve(0, 0):
    print('YES')
    print(n + m - 2)
else:
    print('NO')
