import math
import sys
t = int(input())
for i in range(t):
    n = int(input())
    s1 = 0
    for i in range(1, n // 2):
        s1 += 2 ** i
    s1 += 2 ** n
    s2 = 2 ** (n + 1) - 2 - s1
    print(s1 - s2)
