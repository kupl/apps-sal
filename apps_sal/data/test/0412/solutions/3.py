import sys
n=int(input())
z=list(map(int,input().split()))
max_=0
for i in range(n):
    f=z[i]
    ctr=0
    while True:
        if f%2==0:
            f//=2
            ctr+=1
        else:
            break
    max_=max(max_,ctr)
print(2**max_,end=' ')
ctr=0
f=2**max_
for i in range(n):
    if z[i]%f==0:
        ctr+=1
print(ctr)
