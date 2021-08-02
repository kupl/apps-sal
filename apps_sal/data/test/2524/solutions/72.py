def main():
    N = int(input())
    l = list(map(int, input().split()))
    ans = 0
    m = 10**9 + 7

    for i in range(60):
        x = 0
        for j in l:
            x += 1 & j >> i

        tmp = x * (N - x) % m
        tmp *= 2 ** i % m
        ans += tmp
        ans %= m

    print(ans)


def __starting_point():
    main()


__starting_point()
