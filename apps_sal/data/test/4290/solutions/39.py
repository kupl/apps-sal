def main():
    (n, m) = map(int, input().split())
    cnt = 0
    if m >= 2:
        cnt += m * (m - 1) // 2
    if n >= 2:
        cnt += n * (n - 1) // 2
    print(cnt)


def __starting_point():
    main()


__starting_point()
