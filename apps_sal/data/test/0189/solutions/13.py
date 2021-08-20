n = int(input())
a = [int(t) for t in input().split(' ')]
mincost = 1000 * 100 + 1
best_t = None
for t in range(1, 101):
    cost = 0
    for x in a:
        cost += max(0, abs(x - t) - 1)
    if cost < mincost:
        mincost = cost
        best_t = t
print(best_t, mincost)
