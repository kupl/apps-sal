def main():
    n = int(input())
    ((min1, max1), (min2, max2), (min3, max3)) = list((tuple(map(int, input().split())) for _ in range(3)))
    max1 = min(max1, n - min2 - min3)
    max2 = min(max2, n - max1 - min3)
    print(max1, max2, n - max1 - max2)


def __starting_point():
    main()


__starting_point()
