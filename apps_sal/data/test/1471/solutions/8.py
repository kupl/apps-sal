from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
cost = [[] for _ in range(N+1)]
ans = [-1] * (N+1)

for query in range(N-1):
    u, v, w = map(int, input().split())
    graph[u].append(v)
    cost[u].append(w % 2)
    graph[v].append(u)
    cost[v].append(w % 2)
#print('input')

que = deque()

ans[1] = 0
que.append(1)

while que:
    now = que.popleft()
    #print(graph[now])
    for index in range(len(graph[now])):
        nextg = graph[now][index]
        nextc = cost[now][index]
        #print(ans[nextg])
        if ans[nextg] != -1:
            #print('continued')
            continue
        que.append(nextg)

        #print(nextc)
        if nextc == 1:
            ans[nextg] = (ans[now] + 1) % 2
        else:
            ans[nextg] = ans[now]
    #print(que)
    #print(ans)

#print(ans)

for i in range(1, N+1):
    print(ans[i])
