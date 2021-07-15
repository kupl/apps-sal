import sys
a=[]
b=[]
l=0
val=0
n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
while k>0:
    val=0
    for i in range(n):
        if a[i]<=b[i]:
            b[i]-=a[i]
        else:
            val=val+a[i]-b[i]
            b[i]=0
    if val<=k:
        l+=1
    k-=val
print(l)
