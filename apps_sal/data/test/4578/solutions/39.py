
import math

n, x = map(int, input().split())
minimum = 1000
total = 0
for i in range(n):
    dounats = int(input())
    total += dounats
    if dounats <= minimum:
        minimum = dounats
now = x - total
a = math.floor(now / minimum)
print(n + a)
