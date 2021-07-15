n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    temp=l[i]/m
    l1.append(int(temp+0.9999999))
m=max(l1)
ind=0
for j in range(n):
    if(l1[j]==m):
        ind=j+1
print(ind)
