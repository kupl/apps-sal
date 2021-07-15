import math
t=int(input())
f=[]
for i in range(t):
    n,x=map(int,input().split())
    max1=0
    max2=0
    for i in range(n):
        a,b=map(int,input().split())
        max1=max(max1,a)
        max2=max(max2,a-b)
    if max1>=x:
        f+=[1]
    else:
        if max2>0:
            f+=[1+math.ceil((x-max1)/max2)]
        else:
            f+=[-1]
for i in f:
    print(i)
