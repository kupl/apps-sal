N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
from math import hypot, factorial
distance = []

for i, j in D:
    for k, l in D:
        distance.append(hypot(i-k, j-l))

print((sum(distance)/N))


