def lmi():
    return list(map(int, input().split()))


def main():
    (N, M) = lmi()
    if N == 1 or M == 1:
        print(abs(N - 2) * abs(M - 2))
    else:
        print((N - 2) * (M - 2))


def __starting_point():
    main()


__starting_point()
