import math
from functools import reduce


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


(N, X) = map(int, input().split())
x_list = [X] + list(map(int, input().split()))
x_list.sort()
dist = [0] * (N + 1)
for i in range(N):
    dist[i] += x_list[i + 1] - x_list[i]
ans = gcd_list(dist)
print(ans)
