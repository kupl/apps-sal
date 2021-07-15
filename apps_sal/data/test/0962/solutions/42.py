N,M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    E[a-1].append(b-1)

from collections import deque

d = N+1
flag = False
for i in range(N):
    for v in E[i]:
        q = deque()
        q.append(v)
        used = [N+1]*N
        used[v] = 1
        while q:
            temp = q.popleft()
            if used[temp] > d:
                break
            for u in E[temp]:
                if u == i and d > used[temp]+1:
                    d = used[temp]+1
                    memo = [temp, u]
                    q = deque()
                    flag = True
                    break
                elif u == i:
                    q = deque()
                    break
                if used[u] < N+1:
                    continue
                used[u] = used[temp]+1
                q.append(u)

import heapq
if flag:
    h = []
    dist = [N+1]*N
    dist[memo[1]] = 0
    for v in E[memo[1]]:
        heapq.heappush(h, (1, v))
    while True:
        temp = heapq.heappop(h)
        if dist[temp[1]] < N+1:
            continue
        dist[temp[1]] = temp[0]
        if temp[1] == memo[0]:
            break
        for v in E[temp[1]]:
            if dist[v] < N+1:
                continue
            heapq.heappush(h, (temp[0]+1, v))
    ans = [memo[0]]
    d = dist[memo[0]]-1
    prev = memo[0]
    while d >= 0:
        for i in range(N):
            if dist[i] == d and prev in E[i]:
                prev = i
                ans.append(i)
                d -= 1
                break
    print(len(ans))
    for i in ans:
        print(i+1)
else:
    print(-1)
