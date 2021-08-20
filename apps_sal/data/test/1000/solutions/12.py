(n, v) = list(map(int, input().strip().split()))
remaining_dist = n - 1
adding = min(remaining_dist, v)
cost = adding
remaining_dist -= adding
i = 2
while remaining_dist > 0:
    cost += i
    i += 1
    remaining_dist -= 1
print(cost)
