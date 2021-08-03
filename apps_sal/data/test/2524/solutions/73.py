def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    mod = 10 ** 9 + 7
    for d in range(60):
        # d桁目ごとに考える
        x = 0
        for a in A:
            if (a >> d) & 1:
                x += 1
        ans += x * (n - x) * 2**d
        ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
