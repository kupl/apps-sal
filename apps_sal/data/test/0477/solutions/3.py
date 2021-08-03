def num_steps(x, y):
    if i == x and j == y:
        return 0

    dx = abs(j - y)
    dy = abs(i - x)

    if (dy == 0 and i - a < 1 and i + a > n) or (dx == 0 and j - b < 1 and j + b > m):
        return -1

    if dy % a != 0 or dx % b != 0:
        return -1

    ny = dy // a
    nx = dx // b

    if nx % 2 != ny % 2:
        return -1

    return max(nx, ny)


n, m, i, j, a, b = map(int, input().split())
cand = list(filter(lambda x: x >= 0, (num_steps(1, 1), num_steps(n, 1), num_steps(1, m), num_steps(n, m))))

if not cand:
    print("Poor Inna and pony!")
else:
    print(min(cand))
