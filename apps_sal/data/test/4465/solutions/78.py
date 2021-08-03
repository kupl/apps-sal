def mapt(fn, *args):
    return list(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b = Input()
    print((a - 1) * (b - 1))


main()
