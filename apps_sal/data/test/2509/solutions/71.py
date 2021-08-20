def solve(N, K):
    if K == 0:
        return N ** 2
    else:
        ans = 0
        for b in range(K + 1, N + 1):
            (q, r) = (N // b, N % b)
            ans += q * (b - K) + max(0, r - K + 1)
        return ans


def main():
    (N, K) = list(map(int, input().split()))
    print(solve(N, K))


def __starting_point():
    main()


__starting_point()
