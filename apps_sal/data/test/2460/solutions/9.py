n, m = list(map(int, input().split(' ')))

distances = list(map(int, input().split(' ')))
taxiDriver = list(map(int, input().split(' ')))

people = []
drivers = []
result = [0] * m

for i in range(len(distances)):
    if(taxiDriver[i]):
        drivers.append(distances[i])
    else:
        people.append(distances[i])

j = 0

for person in people:
    if (j + 1) < len(drivers):
        while (j + 1) < len(drivers) and (drivers[j] - person) < (person - drivers[j + 1]):
            j += 1

        result[j] += 1
    else:
        result[j] += 1

print(' '.join(map(str, result)))
