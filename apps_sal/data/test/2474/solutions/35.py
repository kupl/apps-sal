def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    C = list(map(int, input().split(' ')))
    C.sort()
    pow_2 = 1  # 2 ** (2 * N - 2)
    for _ in range(2 * N - 2):
        pow_2 *= 2
        pow_2 %= MOD
    ans = 0
    for k, c in enumerate(C):
        ans += c * ((N - k + 1) * pow_2)
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
