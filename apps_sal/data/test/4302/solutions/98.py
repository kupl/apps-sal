def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b = Input()
    c1 = a + b
    c2 = a + a - 1
    c3 = b + b - 1
    print(max(c1, c2, c3))


main()
