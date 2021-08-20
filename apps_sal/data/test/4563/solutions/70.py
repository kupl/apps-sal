def main():
    N = int(input())
    (T1, A1) = map(int, input().split())
    for _ in range(N - 1):
        (T2, A2) = map(int, input().split())
        n = max(-(-T1 // T2), -(-A1 // A2))
        (T1, A1) = (T2 * n, A2 * n)
    print(T1 + A1)


def __starting_point():
    main()


__starting_point()
