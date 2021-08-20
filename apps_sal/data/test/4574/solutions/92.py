import collections
(_, *a) = map(int, open(0).read().split())
c = collections.Counter(a)
tmp = []
for (k, v) in c.items():
    if v > 3:
        tmp.append(k)
    if v > 1:
        tmp.append(k)
tmp.sort()
print(tmp[-1] * tmp[-2] if len(tmp) > 1 else 0)
