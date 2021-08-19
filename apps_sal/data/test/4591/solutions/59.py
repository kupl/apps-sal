def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (a, b, c, x, y) = Input()
    if a + b < c * 2:
        print(a * x + b * y)
        return
    if x == y:
        print(c * x * 2)
    elif x > y:
        temp = x - y
        print(min(2 * c * x, 2 * c * y + temp * a))
    else:
        temp = y - x
        print(min(2 * c * y, 2 * c * x + temp * b))


main()
