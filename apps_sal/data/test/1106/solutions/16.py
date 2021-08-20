from math import floor


def main():
    n = int(input())
    a = list(map(int, input().split()))
    streets = []
    for i in range(2 ** n, 2 ** (n + 1)):
        idx = i
        if idx > 1:
            res = a[idx - 2]
        while idx > 0:
            idx = int(floor(idx / 2))
            if idx > 1:
                res += a[idx - 2]
        streets.append(res)
    res = 0
    while len(streets) > 2:
        new_streets = []
        for i in range(0, len(streets), 2):
            res += abs(streets[i] - streets[i + 1])
            new_streets.append(max(streets[i], streets[i + 1]))
        streets = new_streets
    print(res + abs(streets[0] - streets[1]))


def __starting_point():
    main()


__starting_point()
