def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    t, a, b = Input()
    print(min(t * a, b))


main()
