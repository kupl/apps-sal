def main():
    (N, X, T) = map(int, input().split())
    cnt = 0
    while N > 0:
        N -= X
        cnt += 1
    print(T * cnt)


def __starting_point():
    main()


__starting_point()
