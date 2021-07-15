from collections import deque,defaultdict
n = int(input())
edges = [[] for _ in range(n)]
for i in range(n-1):
    a,b=list(map(int, input().split()))
    edges[a-1].append([b-1,i])
    edges[b-1].append([a-1,i])
c = 1
col = [0]*(n-1)
visited = [0]*(n-1)
que=deque()
for v in edges[0]:
    que.append(v)
    col[v[1]]=c
    visited[v[1]]=1
    c+=1
while que:
    v=que.popleft()
    c = 1
    used = set()
    for i in edges[v[0]]:
        if(visited[i[1]]):
            used.add(col[i[1]])
    for next_v in edges[v[0]]:
        if(not visited[next_v[1]]):
            if(c in used):
                c+=1
            col[next_v[1]] = c
            used.add(c)
            c+=1
            visited[next_v[1]] = 1
            que.append(next_v)
print((max(col)))
for i in col:
    print(i)

