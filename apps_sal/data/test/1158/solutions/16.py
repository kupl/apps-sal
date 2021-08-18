from collections import Counter
from math import ceil
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
d = Counter()
for i in a:
    d[i] += 1
m = ceil(max(d.values()) / k) * len(d) * k
s = sum(d.values())
print(m - s)
