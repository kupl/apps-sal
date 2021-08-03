def c178(n):

    ans = 0
    mod = 10**9 + 7

    ans = (10**n - 2 * (9**n) + 8**n)

    return ans % mod


def main():
    n = int(input())
    print(c178(n))


def __starting_point():
    main()


__starting_point()
