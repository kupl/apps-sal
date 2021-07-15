n=int(input())
l1=list(map(int,input().split()))
if n%2==0:
    for i in range(n):
        if l1[i]>=0:
            l1[i]=-1*l1[i]-1
else :
    for i in range(n):
        if l1[i]>=0:
            l1[i]=-1*l1[i]-1
    l1[l1.index(min(l1))]=l1[l1.index(min(l1))]*-1 -1
print(' '.join(str(x) for x in l1))
