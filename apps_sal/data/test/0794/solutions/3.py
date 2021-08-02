import math
from collections import deque, defaultdict
from sys import stdin, stdout
#input = stdin.readline
# print = stdout.write
listin = lambda: list(map(int, input().split()))
mapin = lambda: map(int, input().split())
n = int(input())
a = listin()
a.sort()
if len(set(a)) == 1:
    print(-1)
else:
    print(*a)
