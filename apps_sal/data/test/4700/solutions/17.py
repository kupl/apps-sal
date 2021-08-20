def main() -> None:
    (n, m) = list(map(int, input().split()))
    heights = tuple(map(int, input().split()))
    good = [1] * n
    for _ in range(m):
        (a, b) = list(map(int, input().split()))
        (height_a, height_b) = (heights[a - 1], heights[b - 1])
        if height_a == height_b:
            (good[a - 1], good[b - 1]) = (0, 0)
        elif height_a < height_b:
            good[a - 1] = 0
        else:
            good[b - 1] = 0
    print(good.count(1))
    return


def __starting_point():
    main()


__starting_point()
