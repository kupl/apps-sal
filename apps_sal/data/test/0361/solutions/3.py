3


def main():
    s = input()
    c = 'CODEFORCES'
    for i in range(len(c) + 1):
        if s.startswith(c[:i]) and s.endswith(c[i:]):
            print('YES')
            return
    print('NO')


def __starting_point():
    main()


__starting_point()
