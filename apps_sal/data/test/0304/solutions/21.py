from itertools import product
from operator import mul
from functools import reduce
n = input().strip()
c0 = n.count('0')
cc = [n.count(str(i)) for i in range(10)]
cc = [c for c in cc if c > 0]
facs = [1]
for i in range(1, 20):
    facs.append(facs[-1] * i)


def prod(p):
    return reduce(mul, p, 1)


def getC(p):
    return facs[sum(p)] // prod((facs[pp] for pp in p))


def getcount(ct, a0=False):
    its = [list(range(1 - int(a0), ct[0] + 1))] + [list(range(1, cti + 1)) for cti in ct[1:]]
    return sum((getC(p) for p in product(*its)))


if c0 == 0:
    res = getcount(cc)
elif c0 == 1:
    ccr = list(cc)
    del ccr[0]
    res = getcount(cc) - getcount(ccr)
else:
    ccr = list(cc)
    ccr[0] -= 1
    res = getcount(cc) - getcount(ccr, True)
print(res)
