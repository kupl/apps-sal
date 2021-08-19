def mapt(fn, *args):
    return list(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    n = int(input())
    a = Input()
    print(max(a) - min(a))


main()
