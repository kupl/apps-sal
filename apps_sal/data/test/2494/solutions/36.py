from collections import deque
K=int(input())
dist=[10**15 for i in range(K)]
dist[1]=1
q=deque([1])
while(len(q)>0):
    r=q.popleft()
    s=(r+1)%K
    if dist[r]+1<dist[s]:
        dist[s]=dist[r]+1
        q.append(s)
    t=(r*10)%K
    if dist[r]<dist[t]:
        dist[t]=dist[r]
        q.appendleft(t)
print((dist[0]))

