def main():
    s = input()
    if len(s) == 2:
        if s[0] == s[1]:
            print((1, 2))
            return
    for i in range(len(s) - 2):
        if s[i] == s[i + 1]:
            print((i + 1, i + 2))
            break
        elif s[i] == s[i + 2]:
            print((i + 1, i + 3))
            break
    else:
        print((-1, -1))


def __starting_point():
    main()


__starting_point()
