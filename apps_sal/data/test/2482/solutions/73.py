from collections import deque, Counter

N, K, L = [int(s) for s in input().split()]
edge_road = [[int(s) - 1 for s in input().split()] for _ in range(K)]
edge_train = [[int(s) - 1 for s in input().split()] for _ in range(L)]
graph_road = [[] for _ in range(N)]
graph_train = [[] for _ in range(N)]

for i, j in edge_road:
    graph_road[i].append(j)
    graph_road[j].append(i)

for i, j in edge_train:
    graph_train[i].append(j)
    graph_train[j].append(i)

group_road = [0] * N
group_num = 0

visited = [False]*N

for i in range(N):
    if visited[i]:
        continue
    dq = deque([i])
    group_road[i] = group_num
    visited[i] = True
    while(dq):
        search_obj = dq.pop()
        for candidate_obj in graph_road[search_obj]:
            if not visited[candidate_obj]:
                group_road[candidate_obj] = group_num
                dq.appendleft(candidate_obj)
                visited[candidate_obj] = True
    group_num += 1


group_train = [0] * N
group_num = 0

visited = [False]*N

for i in range(N):
    if visited[i]:
        continue
    dq = deque([i])
    group_train[i] = group_num
    visited[i] = True
    while(dq):
        search_obj = dq.pop()
        for candidate_obj in graph_train[search_obj]:
            if not visited[candidate_obj]:
                group_train[candidate_obj] = group_num
                dq.appendleft(candidate_obj)
                visited[candidate_obj] = True
    group_num += 1

group_count = Counter(zip(group_road, group_train))

for gr, gt in zip(group_road, group_train):
    print(group_count[(gr, gt)], end=' ')

