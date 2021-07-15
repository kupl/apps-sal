n,u,v=map(int,input().split())
tree=[[]for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
va=[-1]*n
q=[v-1]
va[v-1]=0
while q:
    x=q.pop()
    for j in tree[x]:
        if va[j]==-1:
            q.append(j)
            va[j]=va[x]+1
q=[u-1]
vt=[-1]*n
vt[u-1]=0
ans=0
while q:
    x=q.pop()
    ans=max(ans,va[x])
    for j in tree[x]:
        if vt[j]==-1:
            if vt[x]+1<va[j]:
                q.append(j)
                vt[j]=vt[x]+1
            elif vt[x]+1==va[j]:
                vt[j]=vt[x]+1
print(ans-1)
