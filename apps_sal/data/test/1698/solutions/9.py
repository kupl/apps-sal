(a, b) = list(map(int, input().split(' ')))
floors = list(map(int, input().split(' ')))
floors.sort()
floors.reverse()
total = 0
while floors != []:
    if len(floors) >= b:
        dist = floors[0] - 1
        goto = floors[b - 1]
        total += dist + goto - 1 + abs(floors[0] - goto)
        floors = floors[b:]
    else:
        dist = floors[0] - 1
        total += 2 * dist
        floors = []
print(total)
