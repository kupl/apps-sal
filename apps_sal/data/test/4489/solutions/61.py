from collections import Counter
import math
import statistics
import itertools
a = int(input())
g = [input() for _ in range(a)]
b = int(input())
g2 = [input() for _ in range(b)]
g.sort()
g2.sort()
count = 1
ans = {}
ans2 = {}
for i in range(len(g) - 1):
    if g[i + 1] == g[i]:
        count += 1
    else:
        ans[g[i]] = count
        count = 1
ans[g[-1]] = count
count = 1
for i in range(len(g2) - 1):
    if g2[i + 1] == g2[i]:
        count += 1
    elif g2[i] in list(ans.keys()):
        ans[g2[i]] -= count
        count = 1
    else:
        ans[g2[i]] = -count
if g2[-1] in list(ans.keys()):
    ans[g2[-1]] -= count
    count = 1
else:
    ans[g2[-1]] = -count
if max(ans.values()) > 0:
    print(max(ans.values()))
else:
    print(0)
