import math
import collections
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

x = ii()
while 1:
    cnt = 0
    for i in range(2, math.ceil(x**(1 / 2)), 1):
        if x % i == 0:
            cnt = 1
            break
    if cnt == 0:
        print(x)
        return
    x += 1
