import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**9

n = int(input())
if n < 100:
    print(n)
    return
a = [[_,set(map(int,list(str(_))))] for _ in range(100)]
c = 99
for k in range(2,11):
    t = (10 ** (k-1))
    for aa in a:
        if aa[0] < t:
            aa[1] = aa[1] | set([0])
    at = a[:]
    for i in range(1,10):
        t = i * (10 ** k)
        for ai, ae in at:
            ac = ai + t
            if ac > n:
                print(c)
                return
            if len(ae) < 2:
                ae = ae | set([i])
            if i in ae and len(ae) < 3:
                c += 1
                a.append([ac,ae])

