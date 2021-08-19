from sys import stdin, stdout
from math import factorial
from math import log10
(k, n, s, p) = map(int, stdin.readline().split())
(l, r) = (0, 10 ** 9)
while r - l > 1:
    m = l + r >> 1
    v = m * p // k
    if v * s >= n:
        r = m
    else:
        l = m
stdout.write(str(r))
