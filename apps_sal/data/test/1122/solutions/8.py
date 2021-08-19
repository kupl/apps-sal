def main():
    (N, M) = list(map(int, input().split()))
    is_odd = N - 1 & 1
    bias = 0
    for (i, distance) in enumerate(range(N - 1, 0, -2)):
        if is_odd and distance <= -distance % N:
            bias = 1
        left = i + 1
        right = left + distance - bias
        print((left, right))
        if i == M - 1:
            return


def __starting_point():
    main()


__starting_point()
