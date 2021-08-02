import os
import sys
import re
import math

(N, K) = [int(n) for n in input().split()]

d = 0
a = K ** 0
while a <= N:
    d += 1
    a *= K

print(d)
