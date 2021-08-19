(time, normal_cost, unlimited_cost) = list(map(int, input().split()))
if normal_cost * time < unlimited_cost:
    total_cost = normal_cost * time
else:
    total_cost = unlimited_cost
print(total_cost)
