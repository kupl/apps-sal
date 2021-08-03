def main():
    for _ in range(8):
        s = input()
        if not s[::2] == s[0] * 4 != s[1] * 4 == s[1::2]:
            print('NO')
            return
    print('YES')


def __starting_point():
    main()


__starting_point()
