n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
g = [i for i in range(1,n)]
g.append(0)
r=[]
c=[0]*n
for i in l2:
    c[i]+=1
for i in l1:
    d = (n-i)%n
    while c[d]==0:
        if c[g[d]]==0:
            g[d]=g[g[d]]
        d = g[d]
    c[d%n]-=1
    r.append((d+i)%n)
print(*r)
