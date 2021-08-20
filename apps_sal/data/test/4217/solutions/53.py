from collections import Counter


def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (n, m) = Input()
    data = [Input()[1:] for _ in range(n)]
    d = Counter((num for row in data for num in row))
    print(sum((value == n for value in d.values())))


main()
