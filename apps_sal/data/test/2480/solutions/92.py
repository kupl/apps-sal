from collections import defaultdict
import bisect
n, k = list(map(int, input().split()))
a = [1] + list(map(int, input().split()))
d = defaultdict(list)
for i in range(n + 1):
    a[i] -= 1
d[a[0] % k].append(0)
for i in range(n):
    a[i + 1] += a[i]
    d[a[i + 1] % k].append(i + 1)
ans = 0
for l in list(d.values()):
    for i, idx in enumerate(l):
        ans += bisect.bisect_left(l, idx + k) - i - 1
print(ans)
