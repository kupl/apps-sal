import collections
(n, m) = map(int, input().split())
g = [[] for _ in range(n + 1)]
cand1 = set()
cand2 = set()
for _ in range(m):
    (a, b) = map(int, input().split())
    g[a].append(b)
    cand1.add(a)
    cand2.add(b)
cand = cand1 & cand2
ans = -1
for i in range(1, n + 1):
    if i not in cand:
        continue
    else:
        q = collections.deque()
        q.append((i, [i]))
        checked = [0] * (n + 1)
        while len(q) != 0:
            (v, chain) = q.popleft()
            if v == i and len(chain) != 1:
                ans = chain[:-1]
            for u in g[v]:
                if u not in cand:
                    continue
                elif checked[u] == 0:
                    checked[u] = 1
                    q.append((u, chain + [u]))
        cand.discard(i)
if ans == -1:
    print(ans)
else:
    print(len(ans))
    for v in ans:
        print(v)
