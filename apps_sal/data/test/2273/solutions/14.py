a=list(map(int,input().split()))
n=a[0]
e=a[1]
g={}
for itr in range(1,n+1):
    g[itr]=[]
for i in range(e):
    a=list(map(int,input().split()))
    g[a[0]].append(a[1])
    g[a[1]].append(a[0])
for itr in range(1,n+1):
    g[itr]=frozenset(g[itr])
a={}
k=1
res=[]
for i in range(1,n+1):
    if len(g[i])==0:
        k=100
        break
    if g[i] in a: 
        res.append(a[g[i]])
    else: 
        a[g[i]]=k
        k+=1
        res.append(a[g[i]])
    if len(a)>3:break
if k!=4 : print(-1)
else: print(*res)
