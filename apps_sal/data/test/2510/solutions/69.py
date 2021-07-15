import sys
sys.setrecursionlimit(1000000)

f=lambda:map(int,input().split())
N,M=map(int,input().split())

# par=[i for i in range(N+1)]
par=[-1]*(N+1)

def find(x):
    if par[x]<0:return(x)
    else:
        par[x]=find(par[x])
        return(par[x])

def unite(x,y):
    #print("unite1",x,y)
    x=find(x)
    y=find(y)
    #print("unite2",x,y)
    if x==y:return # rootが同じなのでマージは必要ない
    if (par[x]>par[y]):x,y=y,x
    par[x]+=par[y]
    par[y]=x
    #print(par)
    return
    
for i in range(M):
    a,b=map(int,input().split())
    unite(a,b)

print(-min(par[1:]))
