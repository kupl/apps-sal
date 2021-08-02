n = int(input())
maxnum = 100500
numbers = [0] * maxnum
points = [0] * maxnum
inputArray = list(map(int, input().split()))
for i in range(n):
    numbers[inputArray[i]] += 1
for i in range(maxnum):
    points[i] = numbers[i] * i

for i in range(maxnum - 3, 0, -1):
    points[i] = max(points[i + 1], points[i] + points[i + 2])

print(points[1])
