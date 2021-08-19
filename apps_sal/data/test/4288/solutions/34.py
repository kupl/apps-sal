def main():
    (a, b, c) = list(map(int, input().split()))
    if a == b and a != c and (b != c) or (a == c and a != b and (b != c)) or (b == c and a != b and (a != c)):
        return 'Yes'
    return 'No'


def __starting_point():
    print(main())


__starting_point()
