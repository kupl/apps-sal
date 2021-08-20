inf = float('inf')
n = int(input())
arr = list(map(int, input().split()))
min_cost = inf
for i in range(-100, 101):
    cost = 0
    for j in arr:
        cost += (j - i) ** 2
    min_cost = min(min_cost, cost)
print(min_cost)
