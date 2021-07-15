def main():
    S = input()
    p = sum([1 for c in S if c == 'p'])
    print(len(S) // 2 - p)


def __starting_point():
    main()
__starting_point()
