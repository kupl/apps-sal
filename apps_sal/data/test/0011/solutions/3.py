from fractions import gcd
n,a,b,p,q=list(map(int,input().split()))
x=n//(a*b//gcd(a,b))
print((n//a-x)*p+(n//b-x)*q+x*max(p, q))

