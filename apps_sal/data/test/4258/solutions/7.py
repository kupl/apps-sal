def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (a, b, k) = Input()
    ans = k // a * b
    print(ans)


main()
