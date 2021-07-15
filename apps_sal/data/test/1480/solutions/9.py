n,k=map(int,input().split())
*a,=map(int,input().split())
g=list(range(n+1))[1:]
n-=1
v=0
for i in a:
    v+=i
    v%=len(g)
    print(g.pop(v),end=' ')

