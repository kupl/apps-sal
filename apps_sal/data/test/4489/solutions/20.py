from collections import defaultdict
d1 = defaultdict(int)
d2 = defaultdict(int)
n = int(input())
for i in range(n):
    d1[input()] += 1
m = int(input())
for i in range(m):
    d2[input()] += 1
ans = 0
for (k, v) in list(d1.items()):
    ans = max(ans, v - d2[k])
print(ans)
