import math
n, d = list(map(int, input().split()))
x = []

for i in range(n):
    xi = [int(s) for s in input().split()]
    x.append(xi)

count = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        distance = 0
        for k in range(d):
            distance += (x[i][k] - x[j][k]) ** 2
        norm = math.sqrt(distance)
        if norm.is_integer():
            count += 1
print(count)

