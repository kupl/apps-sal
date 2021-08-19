def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (a, b, x) = Input()
    print('YES' if a <= x <= a + b else 'NO')


main()
