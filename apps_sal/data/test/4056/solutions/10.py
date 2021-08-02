import math
from functools import reduce

n = int(input())
a = list(map(int, input().split()))
x = reduce(math.gcd, a)

i = 1
cnt = 0
while i * i < x:
    if x % i == 0:
        cnt += 2
    i += 1
if i * i == x:
    cnt += 1
print(cnt)
