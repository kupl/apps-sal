import math
(N, D) = map(int, input().split())
count = 0
for i in range(N):
    (x, y) = map(int, input().split())
    if math.sqrt(x ** 2 + y ** 2) <= D:
        count += 1
print(count)
