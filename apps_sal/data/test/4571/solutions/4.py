def main():
    (N, M) = list(map(int, input().split()))
    ans = (1900 * M + 100 * (N - M)) * pow(2, M)
    print(ans)


def __starting_point():
    main()


__starting_point()
