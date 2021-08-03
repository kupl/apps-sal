k = int(input())
x, y = [int(x) for x in input().strip().split(" ")]
x, y = x - y, x + y


def main():
    if k % 2 == 0:
        if x % 2 != 0:
            return -1
    return to(x, y)


def cc(x, xs):
    if abs(x - xs) <= 2 * k:
        if abs(x + k - xs) % 2 == k % 2:
            if abs(x + k - xs) <= abs(x - k - xs):
                xs = x + k
            else:
                xs = x - k
            return (True, xs)
        else:
            if x > xs:
                xs += k
            else:
                xs -= k
    else:
        if x > xs:
            xs += k
        else:
            xs -= k
    return (False, xs)


def to(x, y):
    rs = []
    xs, ys = 0, 0
    while True:
        if abs(x - xs) == k or abs(y - ys) == k:
            if abs(x - xs) <= k and abs(y - ys) <= k:
                return rs + [(x, y)]
        mm, ys = cc(y, ys)
        if mm:
            if x > xs:
                xs += k
            else:
                xs -= k
        else:
            mm, xs = cc(x, xs)
        rs.append((xs, ys))


def __starting_point():
    jj = main()
    if jj == -1:
        print((-1))
    else:
        print((len(jj)))
        for r in jj:
            print(((r[0] + r[1]) // 2, (r[1] - r[0]) // 2))


__starting_point()
