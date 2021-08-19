def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (n, a, b) = Input()
    n += 1
    data = (i for i in range(1, n) if a <= sum(map(int, list(str(i)))) <= b)
    print(sum(data))


main()
