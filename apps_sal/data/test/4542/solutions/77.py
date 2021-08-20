def main():
    s = input()
    print(sum([1 for i in range(len(s) - 1) if s[i] != s[i + 1]]))


def __starting_point():
    main()


__starting_point()
