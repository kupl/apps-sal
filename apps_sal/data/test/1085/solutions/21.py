def main():
    N = int(input())
    if N <= 3:
        print(N - 1)
        return
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
    ans_2 = 1
    n = 1
    while n ** 2 < N:
        if (N - 1) % n == 0 and ((N - 1) // n) ** 2 > N:
            ans_2 += 1
        n += 1
    print(ans_1 + ans_2)


def __starting_point():
    main()


__starting_point()
