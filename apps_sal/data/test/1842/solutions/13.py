import re, sys, string, operator, functools, fractions, collections
sys.setrecursionlimit(10**7)
dX= [-1, 1, 0, 0,-1, 1,-1, 1]
dY= [ 0, 0,-1, 1, 1,-1,-1, 1]
RI=lambda x=' ': list(map(int,input().split(x)))
RS=lambda x=' ': input().rstrip().split(x)
mod=int(1e9+7)
eps=1e-6
#################################################
a,b,c=RI()
d=pow(b*b-4*a*c, 0.5)
r1=(-b+d)/(2*a)
r2=(-b-d)/(2*a)
if r1<r2:
    r1,r2=r2,r1
print("%.20f\n%.20f" %(r1,r2))





