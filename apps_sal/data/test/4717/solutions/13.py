def main():
    x, a, b = list(map(int, input().split()))
    print(('A' if abs(x - a) < abs(x - b) else 'B'))


def __starting_point():
    main()

__starting_point()
