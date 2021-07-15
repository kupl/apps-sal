bell_cost = list(map(int, input().split()))
bell_cost.sort()
minimum_cost = bell_cost[0] + bell_cost[1]
print(minimum_cost)
