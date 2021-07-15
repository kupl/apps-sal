# einlesen
# dfs für jede cc
#     Zählen, wie viele w/r
#     wenn cooring nicht möglich -> Ergebnis 0
#     sonst 2^w+2^r
M=998244353 
t=int(input())
n,m=0,0
g=[]
v=[]

def dfs(r):
    s=[r]
    v[r]=1
    c=[0,1]
    while s:
        x=s.pop()
        for j in g[x]:
            if v[j]==v[x]:return 0
            if v[j]==-1:
                v[j]=v[x]^1
                c[v[j]]+=1
                s.append(j)
    if c[0]==0 or c[1]==0:return 3
    return ((2**c[0])%M + (2**c[1])%M)%M

o=[]
for i in range(t):
    n,m=map(int,input().split())
    g=[[]for _ in range(n)]
    for _ in range(m):
        a,b=map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    v=[-1]*n
    ox=1
    for j in range(n):
        if v[j]==-1:
            ox=(ox*dfs(j))%M
    o.append(ox)
print('\n'.join(map(str,o)))
