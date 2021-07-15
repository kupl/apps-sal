def ii(): return int(input())
def fi(): return float(input())
def si(): return input()
def mi(): return map(int,input().split())
def li(): return list(mi())

import math

q=ii()
for i in range(q):
    n=ii()
    a=li()
    s=sum(a)
    ans=math.ceil(s/n)
    print(ans)
