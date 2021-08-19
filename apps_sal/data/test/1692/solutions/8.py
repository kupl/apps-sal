import math
from math import *
s = input()
ans = 0
c1 = 0
c2 = 0
for i in range(len(s)):
    c2 = int(s[i])
    if c2 % 4 == 0:
        ans += 1
        # ++ans
    if i == 0:
        continue
    c1 = int(s[i - 1])
    if (c1 * 10 + c2) % 4 == 0:
        ans += i
print(ans)
