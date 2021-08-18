from bisect import bisect
from collections import defaultdict
from math import gcd, sqrt, ceil
from collections import Counter
import sys
sys.setrecursionlimit(10**9)


def dfs(n):
    b[n] = True

    for i in hash[n]:
        if b[i] == False:
            dfs(i)

    top.append(n)


n, m, s = list(map(int, input().split()))

hash = defaultdict(list)

for i in range(m):
    a, b = list(map(int, input().split()))
    hash[a].append(b)

b = [False] * (n + 1)
top = []
for i in range(1, n + 1):
    if not b[i]:
        dfs(i)
b = [False] * (n + 1)
dfs(s)
top.reverse()
count = 0
for i in top:
    if not b[i]:
        count += 1
        dfs(i)

print(count)
