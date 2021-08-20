from collections import *
(n, m) = map(int, input().split())
outs = defaultdict(list)
ins = defaultdict(int)
for _ in range(m):
    (a, b) = map(int, input().split())
    outs[a - 1] += (b - 1,)
    ins[b - 1] += 1
q = deque((i for i in range(n) if ins[i] == 0))
res = []
while q:
    v = q.popleft()
    res += (v,)
    for w in outs[v]:
        ins[w] -= 1
        if ins[w] == 0:
            q.append(w)
print(-(len(res) == n))
