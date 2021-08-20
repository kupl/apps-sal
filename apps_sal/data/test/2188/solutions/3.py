import sys
from bisect import bisect_left
input = sys.stdin.readline


def ii():
    return int(input())


def mi():
    return map(int, input().rstrip().split())


def lmi():
    return list(map(int, input().rstrip().split()))


def li():
    return list(input().rstrip())


def __starting_point():
    n = ii()
    cnta = 0
    cntb = 0
    lista = []
    listb = []
    for i in range(n):
        (a, b) = mi()
        if a > b:
            cntb += 1
            listb.append((a, b, i + 1))
        else:
            cnta += 1
            lista.append((a, b, i + 1))
    if cnta >= cntb:
        lista.sort(key=lambda x: x[0], reverse=True)
        print(len(lista))
        for i in lista:
            print(i[2], end=' ')
        print()
    else:
        listb.sort(key=lambda x: x[1])
        print(len(listb))
        for i in listb:
            print(i[2], end=' ')
        print()


__starting_point()
