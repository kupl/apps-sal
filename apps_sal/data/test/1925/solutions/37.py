def main():
    A, B, N = map(int, input().split())
    x = min(B - 1, N)
    ans = A * x // B - A * (x // B)
    print(ans)


def __starting_point():
    main()


__starting_point()
