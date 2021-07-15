from functools import reduce
n=int(input())
m=int(input())
a=input().split()
a=[int(x) for x in a]
b=input().split()
b=[int(x) for x in b]
k=m
y=1
for i in range(len(a)):
    k=k*a[i]*b[i]
a=[int(x)-1 for x in a]
b=[int(x)-1 for x in b]
for i in range(len(a)):
    y=y*a[i]*b[i]
if(y==0):
    print(-1)
else:
    print((k/y)-m)
    

