n, k = [int(i) for i in input().split()]
points = [int(i) for i in input().split()]
count = 1
distance = 0
i = 1
while i < n:
    distance += points[i] - points[i - 1]
    if k < points[i] - points[i - 1]:
        count = -1
        break
    if k < distance:
        count += 1
        distance = 0
        continue
    i += 1
print(count)

