from fractions import *
x,y,a,b = list(map(int,input().split()))
nok = (x*y)//gcd(x,y)
first = (a // nok) * nok + (nok if a%nok != 0 else 0)
second = (b//nok) * nok
if first > b:
    print(0)
else:
    print((second-first)//nok +(1 if second % nok == 0 else 0))


