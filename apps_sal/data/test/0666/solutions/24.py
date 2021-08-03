from math import *
n = int(input())
per = int(sqrt(n * 2))
k = per * (per + 1) / 2
if k < n:
    n = n - k
    print(int(n))
else:
    print(int(per - (k - n)))
