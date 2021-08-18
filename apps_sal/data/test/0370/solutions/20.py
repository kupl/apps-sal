import random


def copysign(x, y):
    return abs(x) * (1 if y >= 0 else - 1)


def dist(k, x, y):
    if not (abs(x) + abs(y) < 2 * k):
        return None
    if x == y == 0:
        return 0
    elif abs(x) + abs(y) == k:
        return 1
    elif (abs(x) + abs(y)) % 2 == 0:
        return 2
    else:
        return 3


def iterate_neighbors(k, x, y):
    assert abs(x) + abs(y) < 2 * k
    dz = (2 * k - abs(x) - abs(y)) // 2
    for dx in (dz, k - dz):
        dy = k - dx
        yield (dx, dy)
        yield (dx, - dy)
        yield (- dx, dy)
        yield (- dx, - dy)


def solve(k, x, y):
    while True:
        d = dist(k, x, y)
        if d == 0:
            return
        elif d == 1:
            dx = x
            dy = y
        elif d == 2:
            for dx, dy in iterate_neighbors(k, x, y):
                if dist(k, x - dx, y - dy) == 1:
                    break
            else:
                assert False
        elif d == 3:
            while True:
                dx = random.randint(0, k) * random.choice([-1, 1])
                dy = (k - abs(dx)) * random.choice([-1, 1])
                if dist(k, x - dx, y - dy) == 2:
                    break
        else:
            dx = copysign(min(k, abs(x)), x)
            dy = copysign(k - abs(dx), y)
        yield (dx, dy)
        x -= dx
        y -= dy


def main():
    k = int(input())
    x, y = list(map(int, input().split()))
    if k % 2 == 0 and (abs(x) + abs(y)) % 2 != 0:
        print((-1))
        return
    ops = list(solve(k, x, y))
    print((len(ops)))
    x = 0
    y = 0
    for dx, dy in ops:
        x += dx
        y += dy
        print((x, y))


main()
