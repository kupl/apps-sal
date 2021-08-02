import sys
import math

input = sys.stdin.readline
n = int(input())
m = int(input())
a_list = []
a_max = 0
for _ in range(n):
    a = int(input())
    if a_max < a:
        a_max = a
    a_list.append(a)
tmp = 0
for a in a_list:
    tmp += a_max - a
if tmp >= m:
    a_min = a_max
else:
    a_min = a_max + math.ceil((m - tmp) / n)
print(a_min, a_max + m)
