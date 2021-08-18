import math
import sys

n, p = list(map(int, input().split()))
cities = []
for i in range(n):
    x, y, pi = list(map(int, input().split()))
    cities.append(((x, y), pi))

sorted_cities = sorted(cities, key=lambda data: math.sqrt(data[0][0]**2 + data[0][1]**2))
for i in range(n):
    if p < 1000000:
        p += sorted_cities[i][1]
        if p >= 1000000:
            print(math.sqrt(sorted_cities[i][0][0]**2 + sorted_cities[i][0][1]**2))
            return
print(-1)
