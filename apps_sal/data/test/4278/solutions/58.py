from collections import Counter


def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    k = int(input())
    a = sorted([''.join(sorted(input())) for _ in range(k)])
    d = Counter(a)
    return int(sum((val * (val - 1) / 2 for val in d.values())))


print(main())
