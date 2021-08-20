from heapq import heappop, heappush
(N, M, S) = map(int, input().split())
inf = float('inf')
cost = [[] for _ in range(N)]
exc = []
for _ in range(M):
    (u, v, a, b) = map(int, input().split())
    (u, v) = (u - 1, v - 1)
    cost[u].append((v, a, b))
    cost[v].append((u, a, b))
for _ in range(N):
    (c, d) = map(int, input().split())
    exc.append((c, d))
S = min(S, 2450)
di = [inf] * 2451 * N
di[S] = 0
hq = [(0, S)]
while hq:
    (t, v) = heappop(hq)
    u = v // 2451
    s = v % 2451
    if t > di[v]:
        continue
    for (x, a, b) in cost[u]:
        if s >= a:
            v_new = x * 2451 + s - a
            t_new = t + b
            if t_new < di[v_new]:
                di[v_new] = t_new
                heappush(hq, (t_new, v_new))
    (c, d) = exc[u]
    c = min(c, 2450 - s)
    v_new = v + c
    t_new = t + d
    if t_new < di[v_new]:
        di[v_new] = t_new
        heappush(hq, (t_new, v_new))
for i in range(1, N):
    m = min(di[i * 2451:(i + 1) * 2451])
    print(m)
