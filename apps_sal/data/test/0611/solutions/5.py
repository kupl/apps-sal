def main():
    (n, m) = list(map(int, input().split(' ')))
    s = 0
    Ms = n * (n - 1) // 2
    ms = n // 2 * (n // 2 + 1)
    if n % 2 == 0:
        ms -= n // 2
    for _ in range(m):
        (x, d) = list(map(int, input().split(' ')))
        s += x * n
        s += Ms * d if d >= 0 else ms * d
    print(s / n)


def __starting_point():
    main()


__starting_point()
