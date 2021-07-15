from collections import deque
N,M=list(map(int,input().split()))
G=[[] for i in range(N)]
for i in range(M):
    a,b=list(map(int,input().split()))
    G[a-1].append(b-1)
K=[0 for i in range(N)]
for i in range(N):
    for p in G[i]:
        K[p]+=1
q=deque(i for i in range(N) if K[i]==0)
res=[]
while q:
    v1=q.popleft()
    res.append(v1)
    for v2 in G[v1]:
        K[v2]-=1
        if K[v2]==0:
            q.append(v2)
if len(res)==N:
    print((-1))
    return
X={i for i in range(N)}
for st in range(N):
    before=[-1 for i in range(N)]
    q=deque([st])
    flag=0
    while(q):
        r=q.popleft()
        for p in G[r]:
            if before[p]==-1:
                before[p]=r
                q.append(p)
            if before[st]!=-1:
                Y={st}
                tmp=before[st]
                while(tmp!=st):
                    Y.add(tmp)
                    tmp=before[tmp]
                if len(Y)<len(X):
                    X={i for i in Y}
                flag=1
                break
        if flag:
            break
print((len(X)))
for i in X:
    print((i+1))

