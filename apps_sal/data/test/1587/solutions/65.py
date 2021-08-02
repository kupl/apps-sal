def main():
    n = int(input())
    s = input()
    rcount = s.count('R')
    diff = s[0:rcount].count("W")

    print(diff)


def __starting_point():
    main()


__starting_point()
