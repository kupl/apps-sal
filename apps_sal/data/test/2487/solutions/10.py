def main():
    n = int(input())
    x = 0
    y = 0
    for i in range(1, n + 1):
        x += (n - i + 1) * i
    for _ in range(n - 1):
        (u, v) = map(int, input().split())
        if v < u:
            (u, v) = (v, u)
        y += u * (n - v + 1)
    print(x - y)


def __starting_point():
    main()


__starting_point()
