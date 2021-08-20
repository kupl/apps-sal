MAXV = 53


def is_on_border(x_min, x_max, y_min, y_max, x, y):
    if (x == x_min or x == x_max) and (y_min <= y and y <= y_max):
        return True
    return (y == y_min or y == y_max) and (x_min <= x and x <= x_max)


def unique_non_border(p, x_min, x_max, y_min, y_max):
    res = -1
    for i in range(len(p)):
        if not is_on_border(x_min, x_max, y_min, y_max, p[i][0], p[i][1]):
            if res != -1:
                return -1
            res = i
    return res


def sol(p):
    for l in range(1, MAXV + 1):
        for x in range(0, MAXV - l + 1):
            for y in range(0, MAXV - l + 1):
                res = unique_non_border(p, x, x + l, y, y + l)
                if res != -1:
                    return res
    assert False
    return -1


n = int(input())
p = []
for i in range(4 * n + 1):
    (x, y) = list(map(int, input().split()))
    p.append((x, y))
ans = sol(p)
print(*p[ans])
