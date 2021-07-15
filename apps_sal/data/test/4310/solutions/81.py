def mapt(fn, *args):
    return list(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b, c = Input()
    x, y, _ = sorted([abs(a-b), abs(b-c), abs(a-c)])
    print(x + y)


main()
