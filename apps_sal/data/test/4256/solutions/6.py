def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (a, b, c) = Input()
    print(min(b // a, c))


main()
