from collections import deque
n, m = list(map(int, input().split()))
g = [[] for _ in range(n)]
INF = float('inf')
for _ in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    g[a].append(b)

res = []
shortest = n + 1
for s in range(n):
    dist = [-1] * n
    prev = [-1] * n
    q = deque()
    q.append(s)
    dist[s] = 0
    while len(q) != 0:
        v = q.popleft()
        for nv in g[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                prev[nv] = v
                q.append(nv)
    for t in range(n):
        if t == s:
            continue
        if dist[t] == -1:
            continue
        for nt in g[t]:
            if nt == s:
                temp = [s]
                cur = t
                while cur != s:
                    temp.append(cur)
                    cur = prev[cur]
                if shortest > len(temp):
                    shortest = len(temp)
                    res = temp
if shortest == n + 1:
    print((-1))
    return
print((len(res)))
for v in res:
    print((v + 1))

# def bfs(sv):
#     dist = [INF] * n
#     pre = [-1] * n
#     q = deque()
#     q.append(sv)
#     dist[sv] = 0
#     while q:
#         v = q.popleft()
#         for nv in g[v]:
#             if dist[nv] == INF:
#                 continue
#             pre[nv] = v
#             dist[nv] = dist[v] + 1
#             q.append(nv)
#     print(dist)
#     best = (INF, -1)
#     for v in range(n):
#         if v == sv:
#             continue
#         for nv in g[v]:
#             if nv == sv:
#                 best = min(best, (dist[nv], nv))
#                 print(sv, best)
#                 # print(best)
#     if best[0] == INF:
#         return [0] * (n + 1)
#     print(pre)
#     v = best[1]
#     print('v', v)
#     res = []
#     while v != -1:
#         res.append(v)
#         v = pre[v]
#     print('res', res)
#     return res


# ans = [0] * (n + 1)
# for s in range(n):
#     now = bfs(s)
#     if len(now) < len(ans):
#         print('aa')
#         ans = now
#         print(ans)
# if len(ans) == n + 1:
#     print(-1)
#     return
# print(len(ans))
# for v in ans:
#     print(v)

