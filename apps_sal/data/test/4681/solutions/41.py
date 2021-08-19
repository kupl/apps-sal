from collections import defaultdict


def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    n = int(input())
    l = defaultdict(int)
    (l[0], l[1]) = (2, 1)
    for i in range(2, n + 1):
        l[i] = l[i - 1] + l[i - 2]
    print(l[n])


main()
