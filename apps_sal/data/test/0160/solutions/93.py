import math

n,k=map(int,input().split())

A=list(map(int,input().split()))

x=sum(A)

X=[]

for i in range(1,int(math.sqrt(x))+1):
    if x%i==0:
        X.append(i)
        X.append(x//i)
X.sort(reverse=True)

for i in X:
    B=[]
    for j in range(n):
        B.append(A[j]%i)
    B.sort()
    if sum(B[:-1*(sum(B)//i)])<=k:
        print(i)
        break
