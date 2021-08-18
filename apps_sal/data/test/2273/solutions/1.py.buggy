n, m = list(map(int, input().split()))

ad = [[] for _ in range(n)]

es = []
for _ in range(m):
    v, u = list(map(int, input().split()))
    v -= 1
    u -= 1
    es.append((min(v, u), max(v, u)))
es = sorted(es, key=lambda x: (x[0], x[1]))

for e in es:
    v, u = e
    ad[v].append(str(u))
    ad[u].append(str(v))


ad = [''.join(a) for a in ad]
d = {}
for t in ad:
    if t not in d:
        d[t] = str(len(d) + 1)
    if len(d) > 3:
        print(-1)
        return
if len(d) != 3:
    print(-1)
    return

ans = []
for t in ad:
    ans.append(d[t])
print(' '.join(ans))
