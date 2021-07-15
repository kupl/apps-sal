import math
import sys

#imgur.com/Pkt7iIf.png

#n, m = map(int, input().split())
#n = int(input())
#d = list(map(int, input().split()))

n = int(input())
r = 0
t = 1
for i in range(n-1):
    r += t*2
    t += 2
print(r + t)

