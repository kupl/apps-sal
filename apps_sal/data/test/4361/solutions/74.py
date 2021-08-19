def main():
    (N, K) = list(map(int, input().split()))
    H = sorted([int(input()) for _ in range(N)])
    ans = min([H[i + K - 1] - H[i] for i in range(N - K + 1)])
    print(ans)


def __starting_point():
    main()


__starting_point()
