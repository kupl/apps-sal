from math import sqrt
n = int(input())
x = (-1+sqrt(1+8*n))/2
v = (2+int(x)-1)/2*int(x)
if (v==n): print(int(x))
else: print(int(n-v))

