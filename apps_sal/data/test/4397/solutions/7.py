def mapt(fn, *args):
    return list(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, i = Input()
    print(n - i + 1)


main()
