from math import pi, atan2
numMannequins = int(input())
coordinates = []
for i in range(numMannequins):
    coordinates.append(map(int, input().split()))
coordinates = sorted((atan2(y, x) for (x, y) in coordinates))
distance = [coordinates[i + 1] - coordinates[i] for i in range(numMannequins - 1)]
distance.append(2 * pi - coordinates[numMannequins - 1] + coordinates[0])
print(360 - 180 * (max(distance) / pi))
