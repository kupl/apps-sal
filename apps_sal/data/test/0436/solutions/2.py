n=int(input())
l1=list(map(int,input().split()))
total=sum(l1)
res=[1]
s=l1[0]
for i in range(1,n):
    if 2*l1[i]<=l1[0]:
        res.append(i+1)
        s+=l1[i]
if 2*s>total:
    print(len(res))
    print(*res,sep=" ")
else :
    print(0)
