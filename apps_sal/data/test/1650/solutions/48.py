def main():
    l = input()
    n = len(l)
    mod = 10**9 + 7
    dp1 = [0 for i in range(n)]
    dp2 = [0 for i in range(n)]
    dp1[0] = 1
    dp2[0] = 2
    for i in range(1, n):
        if l[i] == '1':
            dp2[i] = (2 * dp2[i - 1]) % mod
            dp1[i] = (3 * dp1[i - 1] + dp2[i - 1]) % mod
        else:
            dp2[i] = dp2[i - 1]
            dp1[i] = (3 * dp1[i - 1]) % mod
    print(((dp1[-1] + dp2[-1]) % mod))


def __starting_point():
    main()


__starting_point()
