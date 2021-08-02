def main():
    mod = 998244353
    N, K = map(int, input().split())
    S = [tuple(map(int, input().split())) for _ in range(K)]
    S.sort()

    f = [0] * N
    f[0] = 1
    a = [0] * (N + 1)
    a[1] = -1

    for i in range(0, N - 1):
        for l, r in S:
            if i + l < N:
                a[i + l] += f[i]
                a[i + l] %= mod
            if i + r + 1 < N:
                a[i + r + 1] -= f[i]
                a[i + r + 1] %= mod
        f[i + 1] = (f[i] + a[i + 1]) % mod
    print(f[-1])


def __starting_point():
    main()


__starting_point()
