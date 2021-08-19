def mapt(fn, *args):
    return list(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (n, k) = Input()
    if n % k == 0:
        print(0)
    else:
        print(1)


main()
