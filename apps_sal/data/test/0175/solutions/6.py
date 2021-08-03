def solve(x, y):
    if (x == 0 or y == 0):
        return (x, y)
    if (x >= 2 * y and y != 0):
        x %= 2 * y
    if (y >= 2 * x and x != 0):
        y %= 2 * x
    if (x == 0 or y == 0):
        return (x, y)
    if (x < 2 * y and y < 2 * x):
        return (x, y)
    return solve(x, y)


x, y = list(map(int, input().split()))
ans = solve(x, y)
print(ans[0], ans[1])
