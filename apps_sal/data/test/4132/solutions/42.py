from math import *
N=int(input())
A=list(map(int,input().split()))
c=A[0]
for i in range(N):
    c=gcd(A[i],c)
print(c)
