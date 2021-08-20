import sys


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return map(int, sys.stdin.readline().split())


def input():
    return sys.stdin.readline().strip()


def main():
    n = int(input())
    a = list(input())
    f = get_array()
    flag = False
    for i in range(n):
        x = int(a[i])
        if x < f[x - 1]:
            flag = True
            a[i] = f[x - 1]
        elif flag == True and x > f[x - 1]:
            break
    print(*a, sep='')


def __starting_point():
    main()


__starting_point()
