n = int(input())

coordinates = []
heights = []
for i in range(n):
    x, h = map(int, input().split())
    coordinates.append(x)
    heights.append(h)

if n == 1:
    answer = 1
else:
    answer = 2
for i in range(1, n - 1):
    if coordinates[i] - heights[i] > coordinates[i - 1]:
        answer += 1
    elif coordinates[i] + heights[i] < coordinates[i + 1]:
        answer += 1
        coordinates[i] += heights[i]
print(answer)
