import collections
N = int(input())
graph = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append([b-1,i])
    graph[b-1].append([a-1,i])

q = collections.deque()
ans = [-1]*(N-1)
q.append([0,-1])
while len(q) != 0:
    tmp = 1
    v, v2 = q.popleft()
    for w, i in graph[v]:
        if ans[i] != -1:
            continue
        if ans[v2] == tmp:
            tmp += 1
        ans[i] = tmp
        tmp += 1
        q.append([w,i])

print(len(set(ans)))
for i in ans:
    print(i)
