N,X = map(int,input().split())
x = list(map(int,input().split()))
x.append(X)
x.sort
d = 0
from math import gcd
for i in range(N):
    d = gcd(d,abs(x[i]-x[i+1]))
print(d)
