import math
N=int(input())
A=list(map(lambda x:x-1,list(map(int,input().split()))))
B=list(map(lambda x:x-1,list(map(int,input().split()))))
a=0
for i in range(N):
    Apart=A[:i]
    order=0
    for aparts in Apart:
        if aparts<A[i]:
            order+=1
    a+=math.factorial(N-i-1)*(A[i]-order)
b=0
for i in range(N):
    Bpart=B[:i]
    order=0
    for bparts in Bpart:
        if bparts<B[i]:
            order+=1
    b+=math.factorial(N-i-1)*(B[i]-order)
print(abs(a-b))
