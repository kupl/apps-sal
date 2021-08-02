def main():
    _ = int(input())
    k = int(input())
    x = list(map(int, input().split()))
    print((sum([min([abs(xi - point) for point in [0, k]]) * 2 for xi in x])))


def __starting_point():
    main()


__starting_point()
