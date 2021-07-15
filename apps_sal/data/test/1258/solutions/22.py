
n = int(input().strip())

g = {}
rg = {}
cnt = {}


for i in range(1, n + 1):
    cnt[str(i)] = 0
    rg[str(i)] = []

for _ in range(n - 2):
    arr = [x for x in input().split()]
    arr.sort()
    a, b, c = arr
    for e in arr:
        cnt[e] += 1
    
    for p, tr in [((a, b), c), ((a, c), b), ((b, c), a)]:
        if p not in g:
            g[p] = []
        rg[tr].append(p)
        g[p].append(tr)
    

cur = None
for k in cnt:
    if cnt[k] == 1:
        cur = k

was = set()
was.add(cur)
res = [cur, ]

ca, cb = rg[cur][0]

if cnt[ca] == 2:
    cur = ca
else:
    cur = cb

was.add(cur)
res.append(cur)

while len(res) != n:
    cur = [res[-1], res[-2]]
    cur.sort()
    cur = tuple(cur)
    for to in g[cur]:
        if to in was:
            continue
        res.append(to)
        was.add(to)

print(' '.join(res))

