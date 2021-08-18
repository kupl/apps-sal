Q = 10**9 + 7


def main():
    n = int(input())
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        ans %= Q
    ans = (ans - pow(2, n - 1, Q)) % Q
    print(ans)


def __starting_point():
    main()


__starting_point()
