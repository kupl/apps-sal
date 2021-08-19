def main():
    (n, d) = map(int, input().split())
    cnt = 0
    xy = [map(int, input().split()) for i in range(n)]
    (x, y) = [list(i) for i in zip(*xy)]
    for i in range(n):
        if x[i] ** 2 + y[i] ** 2 <= d ** 2:
            cnt += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
