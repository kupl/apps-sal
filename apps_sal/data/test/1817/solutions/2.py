from sys import stdin, stdout
from math import factorial
from math import log10
from math import sqrt
n = int(stdin.readline())
values = sorted(list(map(int, stdin.readline().split())))
(l, r) = (0, n - 1)
label = 0
while l != r:
    if not label:
        r -= 1
    else:
        l += 1
    label ^= 1
stdout.write(str(values[l]))
