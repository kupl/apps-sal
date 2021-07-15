N,M=map(int,input().split())
V=[[]for i in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    V[a-1].append(b-1)
    V[b-1].append(a-1)
print('Yes')
p,q=0,[0]
seen=[0]*N
d=[0]*N
while len(q)!=p:
    for i in V[q[p]]:
        if not seen[i]:
            q.append(i)
            d[i]=q[p]+1
        seen[i]+=1
    p+=1
d.pop(0)
for i in d:print(i)
