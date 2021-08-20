from collections import Counter as C
n = int(input())
l = [*map(int, input().split())]
c = C(l)
s = sum(l)
res = []
for (i, e) in enumerate(l):
    if c.get((s - e) / 2, 0) > int((s - e) / 2 == e):
        res.append(str(i + 1))
print(len(res))
print(' '.join(res))
