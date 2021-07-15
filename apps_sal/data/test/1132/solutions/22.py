from collections import Counter

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    g[x - 1].append(y - 1)
    g[y - 1].append(x - 1)

bus = ([2] * (n - 2)) + ([1] * 2)
star = [1] * (n - 1) + [n - 1]

lns = [len(lst) for lst in g]
if lns == [2] * n:
    print("ring topology")
elif Counter(lns) == Counter(bus):
    print("bus topology")
elif Counter(lns) == Counter(star):
    print("star topology")
else:
    print("unknown topology")
