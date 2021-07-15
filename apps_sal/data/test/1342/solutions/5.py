import time
import sys
from math import sqrt

n = int(input())
a = list(map(int, input().split()))

sq = int(sqrt(a[0]))+2
s = set()

for box in range(1, sq):
    if a[0] % box == 0:
        s.add(a[0] // box)
        s.add(a[0] // box - 1)
    else:
        s.add(a[0] // box)

for balls in range(1, sq):
    if a[0] % balls <= a[0] // balls:
        s.add(balls)


for size in sorted(s, reverse=True):
    ans = 0
    for x in a:
        if x / size >= x % size:
            ans += (x+size) // (size+1)
        else:
            break
    else:
        print(ans)
        return

