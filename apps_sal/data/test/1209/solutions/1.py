import math

count = int(input())
numbers = []
for x in range(count):
    numbers.append(float(input()))

total = 0
temp = []
for k in numbers:
    x = int(math.floor(k))
    total += x
    temp.append((x, k))

result = []
for (floor, original) in temp:
    if float(floor) == original or total == 0:
        result.append(floor)
    else:
        total += 1
        result.append(floor + 1)


for g in result:
    print(g)
