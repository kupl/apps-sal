import sys
import math

n = int(sys.stdin.readline())

for i in range(n):
    a, b = [int(x) for x in (sys.stdin.readline()).split()]
    v = 0
    while(a >= 1 and b >= 1):
        if(a < b):
            v += int(b / a)
            b %= a
        else:
            v += int(a / b)
            a %= b
    print(v)
