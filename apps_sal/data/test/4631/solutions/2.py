(nsap, nhum) = map(int, input().split())
ls = list(map(int, input().split()))
sls = set(ls)
candidates = set()
for e in ls:
    if e + 1 not in sls:
        candidates.add(e + 1)
    if e - 1 not in sls:
        candidates.add(e - 1)
level = 1
totdist = 0
res = set()
while len(res) + len(candidates) <= nhum:
    totdist += level * len(candidates)
    level += 1
    for e in candidates:
        res.add(e)
    cand2 = set()
    for e in candidates:
        for dx in (-1, 1):
            if e + dx not in res and e + dx not in sls:
                cand2.add(e + dx)
    candidates = cand2
for i in range(nhum - len(res)):
    res.add(candidates.pop())
    totdist += level
print(totdist)
for e in res:
    print(e, end=' ')
