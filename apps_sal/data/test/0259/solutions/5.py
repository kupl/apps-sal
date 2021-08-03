import math
from sys import stdin, stdout
n, t = map(int, input().split())
time = 1000000
busroute = 0
for i in range(n):
    x, y = map(int, input().split())
    if(t <= x):
        curr = x
    else:
        curr = math.ceil((t - x) / y) * y + x
    if(curr < time):
        time = curr
        busroute = i + 1
print(busroute)
