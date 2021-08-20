from math import sqrt
import itertools


def issq(k):
    k = int(k)
    return k == int(sqrt(k)) ** 2


ns = input().strip()
l = len(ns)


def getsub(ns, it):
    return ''.join((ns[i] for i in it))


def findmin(ns):
    for i in range(l, 0, -1):
        for it in itertools.combinations(list(range(l)), i):
            its = getsub(ns, it)
            if its.startswith('0'):
                continue
            if issq(its):
                return l - i
    return -1


print(findmin(ns))
