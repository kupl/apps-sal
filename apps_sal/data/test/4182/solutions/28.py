import sys
from collections import deque
mapin = lambda: map(int, sys.stdin.readline().split())
listin = lambda: list(map(int, sys.stdin.readline().split()))
inp = lambda: sys.stdin.readline()

N, M, X, Y = mapin()
veca = listin()
vecb = listin()
max_x = -10000
min_y = 10000
for i in veca:
    if max_x < i: max_x = i
for i in vecb:
    if min_y > i: min_y = i
if max_x < min_y and max_x > X and min_y < Y:
    print("No War")
else: print("War")
