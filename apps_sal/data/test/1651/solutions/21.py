def main():
    import math
    S, P = map(int, input().split())
    x = (S + math.sqrt(S**2 - 4 * P)) / 2
    y = (S - math.sqrt(S**2 - 4 * P)) / 2
    if x != int(x):
        return print("No")
    if x <= 0 or y <= 0:
        return print("No")
    print("Yes")


def __starting_point():
    main()


__starting_point()
