import sys

input = sys.stdin.readline


def main():
    A, B, C, D, E, F = list(map(int, input().split()))

    max_concentration = 0
    ans = (100 * A, 0)
    for a in range(0, F + 1, 100 * A):
        for b in range(0, F - a + 1, 100 * B):
            water = a + b
            if water == 0:
                break
            for c in range(0, F - water + 1, C):
                for d in range(0, F - water - c + 1, D):
                    sugar = c + d
                    if sugar > (water // 100) * E:
                        break
                    concentration = (100 * sugar) / (water + sugar)
                    if concentration > max_concentration:
                        max_concentration = concentration
                        ans = (water + sugar, sugar)

    print((" ".join(map(str, ans))))


def __starting_point():
    main()

__starting_point()
