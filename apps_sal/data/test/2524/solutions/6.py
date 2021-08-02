def main():
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    digit = 60

    ans = 0
    for j in range(digit):
        o = 0
        for i in a:
            if (i >> j) & 1:
                o += 1
        ans += o * (n - o) * 2**j
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
