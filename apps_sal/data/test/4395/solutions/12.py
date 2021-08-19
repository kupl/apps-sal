n = int(input())
g = input()
variants = [['R', 'G', 'B'], ['R', 'B', 'G'], ['G', 'R', 'B'], ['G', 'B', 'R'], ['B', 'R', 'G'], ['B', 'G', 'R']]
best_cost = n
best = None
for v in variants:
    cost = 0
    for i in range(n):
        if g[i] != v[i % 3]:
            cost += 1
    if cost < best_cost:
        best_cost = cost
        best = v
print(best_cost)
for i in range(n):
    print(best[i % 3], end='')
print()
