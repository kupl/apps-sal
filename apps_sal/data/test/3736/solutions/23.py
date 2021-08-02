def main():
    s = input()
    print(("NO", "YES")[s == s[::-1] and all(c in "AHIMOTUVWXY" for c in s)])


def __starting_point():
    main()


__starting_point()
