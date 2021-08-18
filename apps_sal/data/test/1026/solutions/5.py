import sys


def input():
    return sys.stdin.readline()


def iinput():
    return int(input())


def rinput():
    return input().split()


def rlinput():
    return [int(i) for i in input().split()]


def main():

    n = iinput()
    b = rlinput()

    q = dict()

    for i in range(n):
        ind = i + 1 - b[i]

        if ind in q:
            q[ind] += b[i]
        else:
            q[ind] = b[i]

    res = 0

    for i in q:
        res = max(res, q[i])

    print(res)


for i in range(1):
    main()
