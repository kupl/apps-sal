from math import floor
(a, b) = [int(i) for i in input().split()]
if a < b:
    print(-1)
else:
    print((a + b) / (2 * floor((a + b) / (2 * b))))
