from math import *
t = int(input())
for z in range(t):
    l, v, x, y = map(int, input().split())
    ans = l // v
    if(x % v == 0):
        ans -= (y // v - x // v + 1)
    else:
        ans -= (y // v - x // v)
    print(ans)
