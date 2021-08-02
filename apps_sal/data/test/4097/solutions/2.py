R = lambda: map(int, input().split())

inf = 10**7

n = int(input())
b = list(R())


def f(a):
    res = 0

    d = a[1] - a[0]
    e = a[1]
    for i in range(2, n):
        e += d
        if abs(a[i] - e) == 1:
            res += 1
        elif a[i] == e:
            continue
        else:
            return inf
    return res


if n <= 2:
    print(0)
else:
    res = inf
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            b[0] += dx; b[1] += dy
            res = min(res, f(b) + abs(dx) + abs(dy))
            b[0] -= dx; b[1] -= dy
    if res == inf: res = -1
    print(res)
