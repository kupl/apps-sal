from math import gcd
import sys

def lcm(x,y):
    return x*y//gcd(x,y)

def count(x):
    res=0
    while True:
        if x%2==0:
            res+=1
            x//=2
        else:
            break
    return res

n,m=list(map(int,input().split()))
A=list(map(int,input().split()))
A=list(set(A))
n=len(A)

A.sort(reverse=True)

temp=A[0]
for i in range(1,n):
    if count(A[i])!=count(temp):
        print((0))
        return
    else:
        temp=lcm(temp,A[i])

ans=m//(temp//2)-m//temp
print(ans)

