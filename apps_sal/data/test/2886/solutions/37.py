def main():
    s = input()
    if len(s) == 2:
        if s[0] == s[1]:
            print((1, 2))
        else:
            print((-1, -1))
        return
    for i in range(len(s) - 2):
        if len(set(list(s[i:i + 3]))) < 3:
            print((i + 1, i + 3))
            return
    print((-1, -1))


def __starting_point():
    main()


__starting_point()
