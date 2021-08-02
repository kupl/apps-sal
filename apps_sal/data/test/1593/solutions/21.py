import math
n, s = map(int, input().split())
locations = []
for i in range(n):
    x, y, k = map(int, input().split())
    locations += [(x * x + y * y, k)]
locations.sort()
for i in range(n):
    s += locations[i][1]
    if s >= 1000000:
        print(math.sqrt(locations[i][0]))
        return
print(-1)
