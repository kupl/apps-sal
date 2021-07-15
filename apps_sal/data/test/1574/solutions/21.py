n,m = list(map(int,input().split()))
d2 = []
od = []
edges = []
for i in range(n):
   d2.append(set())
   od.append(0)
for i in range(m):
    a,b = list(map(int,input().split()))
    edges.append((a-1,b-1))
    d2[a-1].add(b-1)
    d2[b-1].add(a-1)
    od[a-1]+=1
    od[b-1]+=1
minsum = 1000000
for edg in edges:
    a,b=edg
    nerd=d2[a]&d2[b]
    for c in nerd:
        tmpsum=od[a]+od[b]+od[c]-6
        if(tmpsum<minsum):
            minsum=tmpsum
if(minsum==1000000):
    print("-1")
else:
    print(minsum)

