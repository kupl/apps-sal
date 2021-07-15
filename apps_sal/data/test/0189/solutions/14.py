n = int(input())
a = [int(v) for v in input().split()]
a.sort()

def cost1(v, t):
    if v < t - 1:
        return t - 1 - v
    elif v > t + 1:
        return v - (t + 1)
    else:
        return 0

best_t = None
best_cost = 9999999999999

for t in range(1, 101):
    cost = sum(cost1(v, t) for v in a)
    if cost < best_cost:
        best_cost = cost
        best_t = t

print(best_t, best_cost)

