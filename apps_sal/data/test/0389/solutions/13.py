import math
import fractions

def pFactors(n):
        """Finds the prime factors of 'n'"""
        from math import sqrt
        pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n
        if n == 1: return []
        for check in range(2, limit):
             while num % check == 0:
                pFact.append(check)
                num /= check
        if num > 1:
          pFact.append(num)
        return pFact

def solve():
    a , b = map(int, input().split())
    if a == b:
        print(0)
        return
    gcd = fractions.gcd(a, b)
    af = pFactors(a//gcd)
    bf = pFactors(b//gcd)
    res = 0
    for val in af:
        if val == 2 or val == 3 or val == 5:
            res+=1
        else:
            print(-1)
            return
    for val in bf:
        if val == 2 or val == 3 or val == 5:
            res+=1
        else:
            print(-1)
            return
    ares = gcd
    for val in af:
        ares *= val
    bres = gcd
    for val in bf:
        bres *= val
    if ares != a or bres != b:
        #print(ares, bres)
        print(-1)
        return
    print(res)


solve()
