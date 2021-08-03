import sys
import math

n = int(input())

vmaxx = 0
vmaxy = 0
vminx = 31401
vminy = 31401

s = 0
for i in range(n):
    x1, y1, x2, y2 = [int(x) for x in (sys.stdin.readline()).split()]
    vmaxx = max(vmaxx, x2)
    vmaxy = max(vmaxy, y2)
    vminx = min(vminx, x1)
    vminy = min(vminy, y1)
    s += (x2 - x1) * (y2 - y1)

if(s == (vmaxx - vminx) * (vmaxy - vminy) and (vmaxx - vminx) == (vmaxy - vminy)):
    print("YES")
else:
    print("NO")
