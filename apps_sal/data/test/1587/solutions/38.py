def main():
    n = int(input())
    C = input()
    rc = C.count('R')
    rhc = C[:rc].count('R')
    print(rc - rhc)


def __starting_point():
    main()


__starting_point()
