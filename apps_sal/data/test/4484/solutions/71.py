def factorial(n, mod=10**9 + 7):
    a = 1
    for i in range(1, n + 1):
        a = a * i % mod
    return a


def main():
    N, M = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    if abs(N - M) > 1:
        ans = 0
    elif abs(N - M) == 1:
        ans = (factorial(min(N, M))**2 * max(N, M)) % mod
    else:
        ans = (factorial(N)**2 * 2) % mod

    print(ans)


def __starting_point():
    main()


__starting_point()
