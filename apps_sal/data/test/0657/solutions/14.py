def main():
    (a, b) = map(int, input().split())
    (x, y, z) = map(int, input().split())
    need_y = x * 2 + y
    need_b = 3 * z + y
    print(max(0, need_y - a) + max(0, need_b - b))


def __starting_point():
    main()


__starting_point()
