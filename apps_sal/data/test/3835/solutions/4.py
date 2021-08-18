import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
def listin(): return list(map(int, input().split()))
def mapin(): return map(int, input().split())


n = int(input())
z = []
for i in range(n):
    z.append(listin())
first = (z[0][1] * z[0][2]) // z[1][2]
first = int((first**0.5))
a = [first]
for i in range(1, n):
    a.append(z[0][i] // a[0])
print(*a)
