from sys import stdin, stdout
from math import sin, tan, cos
(n, m, k, l) = map(int, stdin.readline().split())
(lb, rb) = (0, n // m + 1)
while rb - lb > 1:
    mid = lb + rb >> 1
    if mid * m - k >= l:
        rb = mid
    else:
        lb = mid
if lb != n // m:
    stdout.write(str(rb))
else:
    stdout.write('-1')
