import math
(n, s) = tuple(map(int, str.split(input())))
cities = list([tuple(map(int, str.split(input()))) for _ in range(n)])
cities.sort(key=lambda city: city[0] ** 2 + city[1] ** 2)
i = 0
extra = 0
while s + extra < 10 ** 6 and i < n:
    (extra, i) = (extra + cities[i][2], i + 1)
if s + extra < 10 ** 6:
    print(-1)
else:
    (x, y, _) = cities[i - 1]
    print(math.sqrt(x ** 2 + y ** 2))
