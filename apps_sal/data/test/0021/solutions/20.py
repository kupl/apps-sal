import sys,math
n=int(input())
z=list(map(int,input().split()))
f=0
d=0
for i in range(n):
    if z[i]==1:
        f=i
    if z[i]==n:
        d=i
bst=0
if math.fabs(d-f)==n-1:
    print(n-1)
    return
bst=max(math.fabs(d),math.fabs(f), math.fabs(n-1-f), math.fabs(n-1-d))
print(int(bst))
