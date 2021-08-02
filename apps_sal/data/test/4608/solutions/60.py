with open(0) as f:
    N, *a = map(int, f.read().split())

from itertools import count
p = 0
seen = {0}
for i in count(1, 1):
    p = a[p] - 1
    if p == 1:
        ans = i
        break
    if p in seen:
        ans = -1
        break
    seen.add(p)
print(ans)
