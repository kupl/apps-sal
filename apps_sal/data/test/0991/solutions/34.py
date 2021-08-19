import math
import heapq
(N, M, S) = map(int, input().split())
Us = [0] * M
Vs = [0] * M
As = [0] * M
Bs = [0] * M
for i in range(M):
    (Us[i], Vs[i], As[i], Bs[i]) = map(int, input().split())
    Us[i] -= 1
    Vs[i] -= 1
V = {}
Ns = max(As) * N
Nv = N * (Ns + 1)
cnt = 0
for i in range(N):
    for ns in range(Ns + 1):
        V[i, ns] = cnt
        cnt += 1
G = [[] for _ in range(Nv)]
if S > Ns:
    S = Ns
for _ in range(M):
    u = Us.pop()
    v = Vs.pop()
    a = As.pop()
    b = Bs.pop()
    for i in range(Ns + 1):
        ns_s = Ns - i
        ns_g = ns_s - a
        if ns_g >= 0:
            G[V[u, ns_s]].append((V[v, ns_g], b))
            G[V[v, ns_s]].append((V[u, ns_g], b))
for i in range(N):
    (c, d) = map(int, input().split())
    for j in range(Ns):
        ns_s = j
        ns_g = j + c
        if ns_g > Ns:
            ns_g = Ns
        G[V[i, ns_s]].append((V[i, ns_g], d))
D = [math.inf] * Nv
q = []
s = V[0, S]
D[s] = 0
heapq.heappush(q, (0, s))
while len(q) > 0:
    (p_cost, p_v) = heapq.heappop(q)
    if D[p_v] < p_cost:
        continue
    for (e_to, e_cost) in G[p_v]:
        if D[e_to] > D[p_v] + e_cost:
            D[e_to] = D[p_v] + e_cost
            heapq.heappush(q, (D[e_to], e_to))
for i in range(1, N):
    ans = min([D[i * (Ns + 1) + v] for v in range(Ns + 1)])
    print(ans)
