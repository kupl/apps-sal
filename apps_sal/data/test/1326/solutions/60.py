def main():
    N = int(input())
    ans = 0
    for x in range(1, int(N ** 0.5) + 1):
        e = N // x
        ans += x * (e * e + e - x * x)
    print(ans)


def __starting_point():
    main()


__starting_point()
