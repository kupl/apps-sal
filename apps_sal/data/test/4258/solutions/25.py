LI = lambda: list(map(int, input().split()))

A, B, T = LI()


def main():
    ans = (T // A) * B
    print(ans)


def __starting_point():
    main()


__starting_point()
