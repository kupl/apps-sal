from queue import Queue
n,m=[int(x) for x in input().split()]
adj=[[] for i in range(n+1)]
for _ in range (m) :
    src,dest=[int(x) for x in input().split()]
    adj[src].append(dest)
    adj[dest].append(src)
vis=[0]*(n+1)
strt , end = [int(x) for x in input().split()]
vis[strt]=1
q=Queue()
q.put(strt)
k=0
while not q.empty() :
    k+=1
    for i in range(q.qsize()) :
        ele=q.get()
        for j in adj[ele] :
            if vis[j]==0 :
                q.put(j)
                vis[j]=k
print(vis[end])
