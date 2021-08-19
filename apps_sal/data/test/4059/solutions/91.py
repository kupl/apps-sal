def parse():
    N = int(input())
    return N


def main():
    N = parse()
    limit_n = 10 ** 6
    ans = 0
    for A in range(1, min(limit_n, N)):
        for B in range(1, min(limit_n, N)):
            if A * B >= N:
                break
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
