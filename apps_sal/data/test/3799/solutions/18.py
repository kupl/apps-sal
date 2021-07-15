def main():
    s = input()

    if s[0] == s[-1]:
        ss = 1
    else:
        ss = 0

    if len(s) % 2 == ss:
        print("Second")
    else:
        print("First")


def __starting_point():
    main()

__starting_point()
