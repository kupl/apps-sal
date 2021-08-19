from collections import defaultdict
n = int(input())
cost = defaultdict(int)
for _ in range(n):
    (a, x) = [int(x) for x in input().split()]
    cost[a] = max(cost[a], x)
m = int(input())
for _ in range(m):
    (a, x) = [int(x) for x in input().split()]
    cost[a] = max(cost[a], x)
print(sum(cost.values()))
