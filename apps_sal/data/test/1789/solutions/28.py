a, b, x, y = list(map(int, input().split()))
if a == b:
    print(x)
if a < b:
    dif = b - a
    print((min(
        # b階まで階段
        dif * y + x,
        # 全部廊下
        dif * 2 * x + x)))
if a > b:
    dif = a - b
    print((min(
        # 廊下だけ
        (2 * dif - 1) * x,
        # 大体階段
        (dif-1) * y + x
    )))

