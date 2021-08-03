import math
3


def solve(n):
    if n == 0:
        return (0, 0)

    k = int(0.5 * (-1 + math.sqrt(1 + 4 * n / 3.0))) + 10
    while 3 * k * (k + 1) >= n:
        k -= 1

    n -= 3 * k * (k + 1) + 1
    x = 1 + 2 * k
    y = 2

    lim = [k] + [k + 1] * 5
    dx = [-1, -2, -1, 1, 2, 1]
    dy = [2, 0, -2, -2, 0, 2]

    i = 0
    while n > 0:
        t = min(n, lim[i])
        x += t * dx[i]
        y += t * dy[i]
        n -= t
        i += 1

    return (x, y)


x, y = solve(int(input()))
print(x, y)

# for i in range(21):
#   print(i, solve(i))
