import math
import statistics
import collections
a = int(input())
g = [input() for _ in range(a)]
g.sort()
ma = 0
count = 1
for i in range(a - 1):
    if g[i] == g[i + 1]:
        count += 1
    else:
        ma = max(ma, count)
        count = 1
ma = max(ma, count)
count = 1
ans = []
for i in range(a - 1):
    if g[i] == g[i + 1]:
        count += 1
    else:
        if count == ma:
            ans.append(g[i])
        count = 1
if count == ma:
    ans.append(g[-1])
for i in ans:
    print(i)
