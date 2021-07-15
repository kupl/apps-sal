from math import sqrt
from math import ceil
def prime_factorization(n):
    pfs = [1]
    i = 2
    for i in range(2, int(ceil(sqrt(n)))):
        while n % i == 0:
            pfs.append(i)
            n //= i
    if n > 0:
        pfs.append(n)
    return pfs


a, b = map(int, input().split())


def bit_search(pfs):
    m = len(pfs)
    ds = set([])
    for i in range(1 << m):
        d = 1
        for j in range(m):
            if i & (1 << m) > 0:
                d *= pfs[m]
        ds.add(d)
    return ds

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

gcdab = gcd(a, b)
#print (gcdab)
pfsab = prime_factorization(gcdab)
#print (pfsab)
pfsabset =set(pfsab)
print (len(pfsabset))
