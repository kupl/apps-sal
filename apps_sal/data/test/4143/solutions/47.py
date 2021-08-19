import math
members = 0
min_value = 10 ** 16
for i in range(6):
    if i == 0:
        members = int(input())
    else:
        current = int(input())
        if current < min_value:
            min_value = current
counter = math.ceil(members / min_value)
counter += 4
print(counter)
