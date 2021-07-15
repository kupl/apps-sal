n = int(input())
s = 0
while s*s <= n:
    s += 1
s -= 1
if n == s*s:
    print(2*s)
    return

d = n-s*s
from math import ceil
print(2*s + ceil(d*1./s))

