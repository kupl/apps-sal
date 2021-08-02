import math
import sys
a, b, x, y = list(map(int, input().split()))
g = math.gcd(x, y)
x //= g
y //= g
l = 0
r = 10**18
while r - l > 1:
    mid = (r + l) // 2
    if x * mid > a or y * mid > b:
        r = mid
    else:
        l = mid
if x * r > a or y * r > b:
    print(l)
else:
    print(r)
