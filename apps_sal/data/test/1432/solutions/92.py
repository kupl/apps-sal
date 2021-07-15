import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

suma=sum(a)
x=[0]*n
tmp=0
for i in range(1,n,2):
    tmp+=a[i]
x[0]=suma-2*tmp

for i in range(1,n):
    x[i]=2*a[i-1]-x[i-1]
for i in x:
    print(i,end=" ")
