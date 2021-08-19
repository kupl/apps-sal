import math
import collections
t = int(input())
for w in range(t):
    (n, x) = (int(i) for i in input().split())
    if n <= 2:
        print(1)
    else:
        print(1 + math.ceil((n - 2) / x))
