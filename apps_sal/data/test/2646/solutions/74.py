import queue
n,m=list(map(int,input().split()))
l=[[] for i in range(n)]

for _ in range(m):
    tempa,tempb=list(map(int,input().split()))
    tempa-=1
    tempb-=1
    l[tempa].append(tempb)
    l[tempb].append(tempa)
que=queue.Queue()
dist=[-1]*n

dist[0]=0
que.put(0)
ans=[0]*n

while not que.empty():
    v=que.get()

    for nv in l[v]:
        if dist[nv]!=-1:
            continue
        dist[nv]=dist[v]+1
        que.put(nv)
        ans[nv]=v
if -1 in dist:
    print('No')
else:
    print('Yes')
    for i in range(1,n):
        print((ans[i]+1))

