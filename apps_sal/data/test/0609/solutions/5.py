__author__ = 'Adela'


def main():
    n = int(input())
    diag = 'A'
    other = 'A'
    for i in range(n):
        for (j, ch) in enumerate(input()):
            if diag == 'A':
                diag = ch
            elif other == 'A':
                other = ch
            elif i == j or i == n - 1 - j:
                if ch != diag:
                    print('NO')
                    return
            elif ch != other:
                print('NO')
                return
    if diag == other:
        print('NO')
    else:
        print('YES')


def __starting_point():
    main()


__starting_point()
