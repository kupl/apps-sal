from collections import defaultdict
n = int(input())
l = list(map(int, input().split()))
d = defaultdict(int)
cost = n - 1
s = 0
for x in l:
    s += x
    d[s] += 1
    cost = min(cost, n - d[s])
print(cost)
