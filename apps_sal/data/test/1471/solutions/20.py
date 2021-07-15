from collections import deque
n=int(input())
uv=[[] for _ in range(n+1)]
for i in range(n-1):
    u,v,w=list(map(int,input().split()))
    uv[u].append([v,w])
    uv[v].append([u,w])
stack=[1]
ans=[-1]*(n+1)
ans[1]=0
while stack:
    x=stack.pop()
    for j in uv[x]:
        if ans[j[0]]==-1:
            if j[1]%2==0:
                ans[j[0]]=ans[x]
            else:
                ans[j[0]]=(ans[x]+1)%2
            stack.append(j[0])

for k in range(1,n+1):
    print((ans[k]))

