def main():
    (N, M) = list(map(int, input().split()))
    skip = N // 2 // 2 + 1 if N % 2 == 0 else None
    count = 0
    (left, right) = (0, N + 1)
    while count < M:
        left += 1
        if left == skip:
            continue
        right -= 1
        print((left, right))
        count += 1


def __starting_point():
    main()


__starting_point()
