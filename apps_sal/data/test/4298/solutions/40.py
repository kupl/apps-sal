def mapt(fn, *args):
    return list(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, d = Input()
    d = 2 * d + 1
    return (n+d-1)//(d)

print(main())
