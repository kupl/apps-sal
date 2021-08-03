from collections import defaultdict
from bisect import bisect_left

n, k, q = map(int, input().split())
a = list(map(int, input().split()))
s = sorted(list(set(a)))
dic = defaultdict(list)
for i, j in enumerate(a):
    dic[j].append(i)

ans = 10**20
use = [-1, n]

for i in range(len(s)):
    l = []
    for j in range(len(use) - 1):
        x, y = use[j], use[j + 1]
        if y - x - 1 >= k:
            l2 = []
            for t in range(x + 1, y):
                l2.append(a[t])
            l2.sort()
            for t in range(y - x - k):
                l.append(l2[t])
    if len(l) >= q:
        l.sort()
        ans = min(ans, l[q - 1] - l[0])
    for j in dic[s[i]]:
        use.insert(bisect_left(use, j), j)
print(ans)
