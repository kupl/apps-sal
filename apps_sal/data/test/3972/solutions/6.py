mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    ans = [0] * (N + 1)
    ans[N] = N
    ans[N - 1] = N * N
    S = 0
    for i in range(N - 2, 0, -1):
        ans[i] = (ans[i + 1] + S + N * (i + 1) + (N - 1) * (N - i - 2)) % mod
        S = (S + ans[i + 2]) % mod
    print((ans[1]))


def __starting_point():
    main()


__starting_point()
