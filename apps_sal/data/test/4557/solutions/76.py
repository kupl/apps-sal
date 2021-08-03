def main():
    a, b, x = list(map(int, input().split()))
    print(('YES' if a <= x and a + b >= x else 'NO'))


def __starting_point():
    main()


__starting_point()
