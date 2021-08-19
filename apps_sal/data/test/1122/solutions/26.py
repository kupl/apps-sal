def main():
    (N, M) = map(int, input().split())
    if N & 1:
        gen = ((i + 1, N - i) for i in range(M))
    else:
        gen = ((i + 1, N - i) if 2 * i < N / 2 - 1 else (i + 1, N - i - 1) for i in range(M))
    [print(*s) for s in gen]


def __starting_point():
    main()


__starting_point()
