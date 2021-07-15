LI = lambda: list(map(int, input().split()))

A, B, C, D = LI()


def main():
    x = max(A, C)
    y = min(B, D)
    ans = max(0, y - x)
    print(ans)


def __starting_point():
    main()

__starting_point()
