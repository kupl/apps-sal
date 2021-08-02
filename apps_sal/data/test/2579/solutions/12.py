from math import *
l, r, x, y, k = map(int, input().split())
_l = ceil(l / k)
_r = floor(r / k)
if((_l > _r) or (_l > y) or (x > _r)):
    print("NO")
else:
    print("YES")
