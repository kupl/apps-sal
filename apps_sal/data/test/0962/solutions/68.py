from collections import*
n, m, *t = map(int, open(0).read().split())
i = [0] * n
o = [[]for _ in i]
for a, b in zip(*[iter(t)] * 2):
    o[a - 1] += b - 1,
    i[b - 1] += 1
q, r = deque(v for v in range(n)if i[v] < 1), []
while q:
    v = q.popleft()
    r += v,
    for w in o[v]:
        i[w] -= 1
        if i[w] == 0:
            q += w,
print(-(len(r) == n))
