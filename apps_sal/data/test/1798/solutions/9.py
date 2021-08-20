from collections import defaultdict
n = input()
t = list(map(int, input().split()))
(p, d) = (defaultdict(int), defaultdict(int))
for (i, x) in enumerate(t, 1):
    if d[x] < 0:
        continue
    if p[x]:
        if d[x] and i != p[x] + d[x]:
            d[x] = -1
        else:
            d[x] = i - p[x]
    p[x] = i
y = list(d.keys())
y.sort()
t = list(('{0} {1}'.format(x, d[x]) for x in y if d[x] >= 0))
print(len(t))
print('\n'.join(t))
