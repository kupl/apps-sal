from collections import deque
n,u,v=list(map(int, input().split()))
edgelist = [[] for i in range(n)]
for i in range(n-1):
    a,b = list(map(int, input().split()))
    edgelist[a-1].append(b-1)
    edgelist[b-1].append(a-1)
dist = [[0,0] for _ in range(n)]
def distance(start, id):
    que=deque()
    visited = [0]*n

    found = False
    que.append([edgelist[start],start])
    while que:
        ver=que.popleft()
        visited[ver[1]]=1
        for next_v in ver[0]:
            if not visited[next_v]:
                dist[next_v][id]=dist[ver[1]][id]+1
                que.append([edgelist[next_v], next_v])
distance(u-1,0)
distance(v-1,1)
dist.sort(key = lambda x:x[1],reverse = True)
ans=0
for i in range(n):
    if dist[i][1]-dist[i][0]>=1:
        print((dist[i][1]-1))
        return

