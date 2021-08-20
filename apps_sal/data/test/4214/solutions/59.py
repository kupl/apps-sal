import math
n = int(input())
p = []
for i in range(n):
    (x, y) = map(int, input().split())
    p.append([x, y])
ans = 0
for i in range(n):
    for j in range(n):
        ans += math.factorial(n - 1) * math.sqrt((p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2)
print(ans / math.factorial(n))
