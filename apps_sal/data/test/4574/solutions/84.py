import heapq
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
l = []
for i in set(a):
    if c[i] >= 2:
        for j in range(c[i] // 2):
            l.append(i)
if len(l) >= 2:
    print(heapq.nlargest(2, l)[0] * heapq.nlargest(2, l)[1])
else:
    print(0)
