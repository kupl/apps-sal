import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**10
mod = 10**9 + 7

def f():
    n = int(input())
    s = input()
    f = False
    r = 0
    r2 = 0
    sc = ''
    for c in s:
        if c == '(':
            for ss in sc.split('_'):
                r = max(r, len(ss))
            sc = ''
        elif c == ')':
            r2 += len([_ for _ in sc.split('_') if len(_) > 0])
            sc = ''
        else:
            sc += c
    for ss in sc.split('_'):
        r = max(r, len(ss))
    return '{0} {1}'.format(r,r2)

print(f())

