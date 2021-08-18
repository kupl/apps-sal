from collections import Counter

n, x = list(map(int, input().split()))

b = Counter(list(map(int, input().split())))

bs = set(b.keys())


if b.most_common(1)[0][1] > 1:
    print(0)
    return

k = Counter([a & x for a in list(b.keys()) if a & x != a])
ks = set(k.keys())
if len(ks.intersection(bs)) > 0:
    print(1)
    return

if len(k) > 0 and k.most_common(1)[0][1] > 1:
    print(2)
    return
print(-1)
