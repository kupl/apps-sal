n = int(input())
l = list(map(int, input().split()))
d = {}
for a in l:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
ks = sorted(d, reverse=True)
f = 0
for i, k in enumerate(ks):
    if d[k] >= 4:
        print((k * k))
        return
    if d[k] >= 2:
        f = k
        break
s = 0
for k in ks[i + 1:]:
    if d[k] >= 2:
        s = k
        break
print((f * s))
