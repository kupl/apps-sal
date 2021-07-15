import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

x=input()
plus = x.count('+')
minus = x.count('-')
x=input()
plus_ = x.count('+')
minus_ = x.count('-')
n=x.count('?')
a=plus-plus_
b=minus-minus_
if(a<0 or b<0 or a+b!=n):
    print(0.0)
else:
    print(nCr(n,a)/(1<<n))
