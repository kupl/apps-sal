def main():
    (N, K) = list(map(int, input().split(' ')))
    ans = 0
    for b in range(K + 1, N + 1):
        ans += N // b * (b - K)
        ans += max([0, N % b - K + 1])
        if K == 0:
            ans -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
