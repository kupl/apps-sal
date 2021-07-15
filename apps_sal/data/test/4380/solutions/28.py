def main():
    a, b = list(map(int, input().split()))
    for c in range(1, 4):
        if a * b * c % 2 == 1:
            print('Yes')
            return
    print('No')


def __starting_point():
    main()
__starting_point()
