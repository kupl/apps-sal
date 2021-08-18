
costs = input().split(" ")
costs = [int(x) for x in costs]
data = input().split(" ")
totalBuses = int(data[0])
totalTrolleys = int(data[1])
buses = input().split(" ")
trolleys = input().split(" ")
buses = [int(x) for x in buses]
trolleys = [int(x) for x in trolleys]

possibleCosts = [0, 0, 0, 0]

totalBusTravels = sum(buses)
totalTrolleysTravels = sum(trolleys)

cost = [0, 0]
for busCost in buses:
    if busCost * costs[0] > costs[1]:
        cost[0] += costs[1]
    else:
        cost[0] += busCost * costs[0]
if cost[0] > costs[2]:
    cost[0] = costs[2]
for trolleyCost in trolleys:
    if trolleyCost * costs[0] > costs[1]:
        cost[1] += costs[1]
    else:
        cost[1] += trolleyCost * costs[0]
if cost[1] > costs[2]:
    cost[1] = costs[2]

if cost[0] + cost[1] > costs[3]:
    print(costs[3])
else:
    print(cost[0] + cost[1])
