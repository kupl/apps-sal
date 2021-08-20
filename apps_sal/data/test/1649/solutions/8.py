import sys
import itertools
a = list(map(int, input().split()))
su = sum(a)
for pt in itertools.product(range(2), repeat=4):
    if sum(pt) == 0:
        continue
    now = 0
    for (i, x) in enumerate(pt):
        if x:
            now += a[i]
    if now * 2 == su:
        print('Yes')
        break
else:
    print('No')
