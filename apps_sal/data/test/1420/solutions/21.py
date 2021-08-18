n, l = [int(x) for x in input().split(' ')]
locations = [int(x) for x in input().split(' ')]
locations = sorted(locations)
minimum = 0
a = 0
b = 1
while b < n:
    minimum = max(minimum, (locations[b] - locations[a]) / 2)
    a += 1
    b += 1
minimum = max(minimum, locations[0], l - locations[-1])
print(minimum)
