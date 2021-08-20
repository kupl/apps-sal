def main():
    (n, m) = [int(x) for x in input().split()]
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    vv = max(a[0] * b[0], a[-1] * b[0], a[0] * b[-1], a[-1] * b[-1])
    if vv == a[0] * b[0] or vv == a[0] * b[-1]:
        a.pop(0)
    else:
        a.pop(-1)
    vv = max(a[0] * b[0], a[-1] * b[0], a[0] * b[-1], a[-1] * b[-1])
    print(vv)


def __starting_point():
    main()


__starting_point()
