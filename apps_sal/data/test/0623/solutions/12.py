import functools
import math
import sys

a1, a2 = map(int, input().split())
ans = 0
while a1 * a2 != 0:
    if a1 == 1 and a2 == 1:
        break
    if a1 > a2:
        a1 -= 2
        a2 += 1
    else:
        a1 += 1
        a2 -= 2
    ans += 1
print(ans)
