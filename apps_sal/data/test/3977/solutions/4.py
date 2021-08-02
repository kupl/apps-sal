import sys
from copy import deepcopy
input = sys.stdin.readline
v, e, g = list(map(int, input().split()))
connect = [set() for i in range(v)]
gov = list(map(int, input().split()))
for i in range(e):
    x, y = list(map(int, input().split()))
    connect[x - 1].add(y)
    connect[y - 1].add(x)
sizes = []
for i in gov:
    reached = {i}
    while True:
        old = deepcopy(reached)
        for j in range(v):
            if j + 1 in reached:
                reached.update(connect[j])
            elif not connect[j].isdisjoint(reached):
                reached.add(j + 1)
        if old == reached:
            break
    sizes.append(len(reached))
ans = -e
for i in sizes:
    ans += i * (i - 1) // 2
big = max(sizes)
for i in range(v - sum(sizes)):
    ans += big
    big += 1
print(ans)
