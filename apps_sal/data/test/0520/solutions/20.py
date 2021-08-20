def main():
    n = input()
    xs = sorted((int(x) for x in input().split()))
    print(xs[len(xs) // 2])


def __starting_point():
    main()


__starting_point()
