def main():
    (a, b, m) = list(map(int, input().split()))
    if a > b:
        (a, b) = (b, a)
    if m <= b:
        print(0)
        return
    if b <= 0:
        print(-1)
        return
    i = max((b - a) // b, 0)
    a += b * i
    while b < m:
        (a, b, i) = (b, a + b, i + 1)
    print(i)


def __starting_point():
    main()


__starting_point()
