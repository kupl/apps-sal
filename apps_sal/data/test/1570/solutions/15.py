def __starting_point():
    (k, n, w) = map(int, input().split())
    price = (w + 1) * w * k // 2
    print(max(0, price - n))


__starting_point()
