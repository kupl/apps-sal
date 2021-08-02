import math
from statistics import mean

n = int(input())
a = list(map(int, input().split()))

m = mean(a)
if m - math.floor(m) < 0.5:
    m = math.floor(m)
else:
    m = math.floor(m) + 1

diff = 0
for v in a:
    diff += (m - v) ** 2

print(diff)
