def main():
    N = int(input())
    if N <= 3:
        print(N - 1)
        return
    # (1) 2 <= k <= sqrt(N) で題意を満たすkの個数
    ans_1 = 0
    k = 2
    while k ** 2 <= N:
        n = N
        while n % k == 0:
            n //= k
        n %= k
        if n == 1:
            ans_1 += 1
        k += 1
    # (2) sqrt(N) < k <= N で題意を満たすkの個数
    # sqrt(N)より大きいN-1の約数の個数 + 1 (k = N)
    ans_2 = 1
    n = 1
    while n ** 2 < N:
        if (N - 1) % n == 0 and ((N - 1) // n) ** 2 > N:
            ans_2 += 1
        n += 1
    # 答え
    print(ans_1 + ans_2)


def __starting_point():
    main()
__starting_point()
