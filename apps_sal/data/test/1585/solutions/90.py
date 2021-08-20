def main():
    (X, Y) = list(map(int, input().split()))
    ans = 0
    while X <= Y:
        X *= 2
        ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
