def main():
    (A, B, C, D, E, F) = map(int, input().split())
    water = set()
    sugar = set()
    for i in range(F // (100 * A) + 1):
        for j in range(F // (100 * B) + 1):
            water_amount = 100 * A * i + 100 * B * j
            if 0 < water_amount and water_amount <= F:
                water.add(water_amount)
    for i in range(F // C + 1):
        for j in range(F // D + 1):
            sugar_amount = C * i + D * j
            if sugar_amount <= F:
                sugar.add(sugar_amount)
    max_c = -1
    max_w = 0
    max_s = 0
    for w in water:
        for s in sugar:
            if w + s <= F:
                if s / w <= E / 100:
                    if s * 100 / (w + s) > max_c:
                        max_c = s * 100 / (w + s)
                        max_w = w
                        max_s = s
    print(max_w + max_s, max_s)


def __starting_point():
    main()


__starting_point()
