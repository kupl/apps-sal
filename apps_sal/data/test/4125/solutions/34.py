import math
(N, X) = map(int, input().split())
cities = list(map(lambda x: int(x) - X, input().split()))
res = abs(cities[0])
for i in range(1, N):
    res = math.gcd(res, cities[i])
print(res)
