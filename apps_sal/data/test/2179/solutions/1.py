import heapq
n,m = list(map(int, input().split()))
g = [[] for i in range(n)]
for i in range(1,m+1):
    x,y,z = list(map(int, input().split()))
    x -= 1
    y -= 1
    g[x].append((y,z,i))
    g[y].append((x,z,i))
v = int(input())-1
q = [(0,0,v,0)]
s = []
u = [0] * n
a = 0
while len(q) :
    d,l,x,e = heapq.heappop(q)
    if not u[x]:
        u[x] = 1
        s.append(str(e))
        a += l
        for i,k,f in g[x]:
            if not u[i]:
                heapq.heappush(q, (d+k,k,i,f))
print(a)
print(' '.join(s[1:]))




