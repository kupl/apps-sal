from collections import deque

m, k = list(map(int, input().split()))

G = [set() for _ in range(m + 1)]

q, nq = deque(), deque()

for _ in range(m - 1):
    u, v = list(map(int, input().split()))
    G[u].add(v)
    G[v].add(u)

for u in range(1, m + 1):
    if len(G[u]) == 1:
        q.append(u)

step = 0
removed = 0
ok = True

while removed < m - 1:
    each = {}
    for u in q:
        nxt = G[u].pop()
        G[nxt].remove(u)
        each[nxt] = each.get(nxt, 0) + 1
        removed += 1
        if len(G[nxt]) == 0:
            break
        if len(G[nxt]) == 1:
            nq.append(nxt)
    if any(v < 3 for k, v in list(each.items())):
        ok = False
        break
    q, nq = nq, deque()
    step += 1

if ok and step == k and removed == m - 1:
    print('Yes')
else:
    print('No')
