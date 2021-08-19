from sys import stdin
from bisect import bisect_left
stdin.readline()
(x, l) = (0, [])
for y in map(int, stdin.readline().split()):
    x += y
    l.append(x)
stdin.readline()
for y in map(int, stdin.readline().split()):
    print(bisect_left(l, y) + 1)
