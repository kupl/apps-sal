def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    r, d, x = Input()
    for _ in range(10):
        x = x * r - d
        print(x)


main()
