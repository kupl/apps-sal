a, b = list(map(int, input().split()))

numbers = []
for i in range(1, 1000):
    numbers.append(i)

steel_towers = []
for i in range(999):
    steel_towers.append(sum(numbers[:i + 1]))

print((steel_towers[b - a - 1] - b))
