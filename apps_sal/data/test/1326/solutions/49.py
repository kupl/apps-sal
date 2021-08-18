def main():
    N = int(input())
    ans = 0
    for x in range(1, N + 1):
        e = N // x
        ans += x * e * (1 + e) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
