n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
t=[]
ans=0
for i in range(n):
    t.append(v[i]-c[i])
    if t[i]>0:
        ans+=t[i]
print(ans)
