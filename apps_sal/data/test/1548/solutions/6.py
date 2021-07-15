import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
n = int(input())
a = listin()
a.sort()
x, y = 0, 0
a = deque(a)
for i in range(n):
    if i%2:
        y+=a.popleft()
    else:
        x+=a.pop()
print(x**2+y**2)
