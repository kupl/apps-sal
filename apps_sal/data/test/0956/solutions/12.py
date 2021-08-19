import sys
from math import ceil, floor


def main():
    (n, k) = [int(i) for i in input().split()]
    cf = {}
    pf = {}
    for i in range(n):
        (pers1, pers2) = [int(i) for i in input().split()]
        if cf.get(pers1) == None:
            cf[pers1] = set()
            pf[pers1] = set()
        cf[pers1].add(pers2)
        if cf.get(pers2) == None:
            cf[pers2] = set()
            pf[pers2] = set()
        cf[pers2].add(pers1)
    persons = list(cf.keys())
    z = len(persons)
    for i in range(z):
        for j in range(0, z):
            pers1 = persons[i]
            pers2 = persons[j]
            if pers1 != pers2 and pers2 not in cf[pers1]:
                m = 0
                for pers3 in cf[pers1]:
                    if pers2 in cf[pers3]:
                        m += 1
                y = 100 * m / len(cf[pers1])
                if y >= k:
                    pf[pers1].add(pers2)
    persons = sorted(persons)
    for pers in persons:
        print(pers, end='')
        print(':', end=' ')
        print(len(pf[pers]), end=' ')
        ids = sorted(list(pf[pers]))
        for id in ids:
            print(id, end=' ')
        print()


def __starting_point():
    main()


__starting_point()
