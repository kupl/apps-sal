import math

n, s = [int(c) for c in input().split()]

ar = []

for i in range(n):
    x, y, count = [int(c) for c in input().split()]
    ar.append([math.sqrt(x**2 + y**2), count])

ar.sort(key=lambda _: _[0])

i = 0

while i < n and s < 10 ** 6:
    s += ar[i][1]
    i += 1

if s < 10 ** 6:
    print(-1)
else:
    print(round(ar[i - 1][0], 7))
