n,m=list(map(int,input().split()))

uf=[i for i in range(n+1)]

def uf_find(x):
    while uf[x]!=x:
        x=uf[x]
    return x

for i in range(m):
    x,y,z=list(map(int,input().split()))
    a,b=uf_find(x),uf_find(y)
    if a>b:
        a,b=b,a
    uf[b]=a

c=set()
for i in range(1,n+1):
    c.add(uf_find(i))
print((len(c)))

