from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
d = c.copy()
k = c.keys()
for i in k:
    d[i] = c[i] * (c[i] - 1) // 2
s = sum(list(d.values()))
for i in a:
    print(s - d[i] + max(0, (c[i] - 1) * (c[i] - 2) // 2))
