import math
line = input().split()
n = int(line[0])
m = int(line[1])
inhabited_localities = [int(x) for x in input().split()]
columns = [int(x) for x in input().split()]
max_distance = 0
current_distanse = 0
j = 0
for i in inhabited_localities:
    while j < m - 1 and i > columns[j]:
        j += 1
    if j != 0:
        current_distanse = min(abs(columns[j] - i), abs(columns[j - 1] - i))
    else:
        current_distanse = abs(columns[j] - i)
    if max_distance < current_distanse:
        max_distance = current_distanse
print(max_distance)
