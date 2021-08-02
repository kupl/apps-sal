BORDER = 10 ** 10


def get_type(x, y):
    if x == 0:
        return 1 if y > 0 else 5
    if y == 0:
        return 3 if x > 0 else 7
    if x == -y:
        return 0 if y > 0 else 4
    if x == y:
        return 2 if y > 0 else 6
    return -1


def __starting_point():
    n, = list(map(int, input().split()))
    x0, y0 = list(map(int, input().split()))
    check = False
    block = [(-BORDER, BORDER), (0, BORDER), (BORDER, BORDER), (BORDER, 0), (BORDER, -BORDER), (0, -BORDER), (-BORDER, -BORDER), (-BORDER, 0)]
    killer = [None for _ in range(8)]
    for _ in range(n):
        f, xs, ys = input().split()
        x, y = list(map(int, (xs, ys)))
        x, y = x - x0, y - y0
        tp = get_type(x, y)
        if tp < 0:
            continue
        if ((f == 'B' and tp % 2 == 1) or (f == 'R' and tp % 2 == 0)):
            if abs(block[tp][0]) + abs(block[tp][1]) > abs(x) + abs(y):
                block[tp] = (x, y)
        else:
            if abs(block[tp][0]) + abs(block[tp][1]) < abs(x) + abs(y):
                continue
            if killer[tp] is None:
                killer[tp] = (x, y)
                continue
            if abs(killer[tp][0]) + abs(killer[tp][1]) > abs(x) + abs(y):
                killer[tp] = (x, y)
                continue
    for tp in range(8):
        if killer[tp] is None:
            continue
        if abs(killer[tp][0]) + abs(killer[tp][1]) < abs(block[tp][0]) + abs(block[tp][1]):
            check = True
            break
    if check:
        print("YES")
    else:
        print("NO")


__starting_point()
