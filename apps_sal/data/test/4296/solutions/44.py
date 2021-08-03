def main():
    A = list(map(int, input().split()))
    print(('win' if sum(A) <= 21 else 'bust'))


def __starting_point():
    main()


__starting_point()
