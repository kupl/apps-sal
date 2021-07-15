import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
x, y, z = mapin()
if x == y and z == 0:
    print(0)
else:
    if abs(x-y) > z:
        if x-y > 0:
            print('+')
        else:
            print('-')
    else:
        print('?')
