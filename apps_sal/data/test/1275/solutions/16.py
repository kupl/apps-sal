def solve(N, K):
    tmp = 0
    for ab in range(2, 2 * N + 1):
        cd = ab - K
        tmp += sub(N, ab) * sub(N, cd)
    return tmp


def sub(N, K):
    if K - 1 < 0:
        return 0
    elif 0 <= K - 1 <= N:
        return K - 1
    elif N < K - 1:
        return max(0, K - 1 - 2 * (K - 1 - N))


def main():
    (N, K) = list(map(int, input().split()))
    a = solve(N, K)
    print(a)


def __starting_point():
    main()


__starting_point()
