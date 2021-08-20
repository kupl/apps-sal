def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    n = int(input())
    data = sorted((int(input()) for _ in range(n)))
    (x, y) = (data[:-1], data[-1])
    print(sum(x) + y // 2)


main()
