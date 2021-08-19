def b174(n, d, xylist):
    count = 0
    for xy in xylist:
        if (xy[0] ** 2 + xy[1] ** 2) ** 0.5 <= d:
            count += 1
    return count


def main():
    (n, d) = map(int, input().split())
    xylist = [list(map(int, input().split())) for _ in range(n)]
    print(b174(n, d, xylist))


def __starting_point():
    main()


__starting_point()
