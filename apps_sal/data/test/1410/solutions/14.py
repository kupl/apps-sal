import sys
n=int(input())
a=[]
a1=[int(x) for x in input().split()]
a2=[int(x) for x in input().split()]
a3=[int(x) for x in input().split()]
a=[[0],a1,a2,a3]
#print(a)
adj=[[] for i in range(n+1)]
for i in range(n-1):
    u,v=list(map(int,input().split()))
    adj[u].append(v)
    adj[v].append(u)
#print(adj)    
for i in adj:
    if len(i)>2:
        print(-1)
        return
sumi=[0 for i in range(7)]
g=[[0 for j in range(n+1)] for i in range(6)]
for i in range(n):
    if len(adj[i])==1:
        p=i
        break
g[0][p]=1
g[0][adj[p][0]]=2
flag=3
i=adj[p][0]
for _ in range(n-1):
    if len(adj[i])==1:
        break
    if g[0][adj[i][0]]==0 :
        g[0][adj[i][0]]=flag
        flag=6-flag-g[0][i]
        i=adj[i][0]
    else:
        g[0][adj[i][1]]=flag
        flag=6-flag-g[0][i]
        i=adj[i][1]
g[1][p]=2
g[1][adj[p][0]]=3
flag=1
i=adj[p][0]
for _ in range(n-1):
    if len(adj[i])==1:
        break
    if g[1][adj[i][0]]==0 :
        g[1][adj[i][0]]=flag
        flag=6-flag-g[1][i]
        i=adj[i][0]
    else:
        g[1][adj[i][1]]=flag
        flag=6-flag-g[1][i]
        i=adj[i][1]
g[2][p]=1
g[2][adj[p][0]]=3
flag=2
i=adj[p][0]
for _ in range(n-1):
    if len(adj[i])==1:
        break
    if g[2][adj[i][0]]==0 :
        g[2][adj[i][0]]=flag
        flag=6-flag-g[2][i]
        i=adj[i][0]
    else:
        g[2][adj[i][1]]=flag
        flag=6-flag-g[2][i]
        i=adj[i][1]
        
g[3][p]=3
g[3][adj[p][0]]=2
flag=1
i=adj[p][0]
for _ in range(n-1):
    if len(adj[i])==1:
        break
    if g[3][adj[i][0]]==0 :
        g[3][adj[i][0]]=flag
        flag=6-flag-g[3][i]
        i=adj[i][0]
    else:
        g[3][adj[i][1]]=flag
        flag=6-flag-g[3][i]
        i=adj[i][1]

g[4][p]=3
g[4][adj[p][0]]=1
flag=2
i=adj[p][0]
for _ in range(n-1):
    if len(adj[i])==1:
        break
    if g[4][adj[i][0]]==0 :
        g[4][adj[i][0]]=flag
        flag=6-flag-g[4][i]
        i=adj[i][0]
    else:
        g[4][adj[i][1]]=flag
        flag=6-flag-g[4][i]
        i=adj[i][1]

g[5][p]=2
g[5][adj[p][0]]=1
flag=3
i=adj[p][0]
for _ in range(n-1):
    if len(adj[i])==1:
        break
    if g[5][adj[i][0]]==0 :
        g[5][adj[i][0]]=flag
        flag=6-flag-g[5][i]
        i=adj[i][0]
    else:
        g[5][adj[i][1]]=flag
        flag=6-flag-g[5][i]
        i=adj[i][1]
#print(g) 
maxi=10**9*n+5
ans=0
i=1
for j in range(6):
    sumi=0
    
    for i in range(1,n+1):
        #print(i,j,g[j][i])
        sumi+=a[g[j][i]][i-1]
   # print(sumi)    
    if maxi>sumi  :
        maxi=sumi
        ans=j
        
print(maxi)
print(*g[ans][1:])


