n,m=map(int,input().split())
a=[]
ans1=0
for i in range(n):
    a.append(input())
ans=list(map(int,input().split()))
for i in range(m):
    d={}
    ma=-1
    for j in range(n):
        d[a[j][i]]=d.get(a[j][i],0) + 1
        ma=max(ma,d[a[j][i]])
    ans1+=ma*ans[i]
print(ans1)    
