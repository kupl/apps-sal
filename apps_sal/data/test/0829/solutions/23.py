"""input
6
100011
"""
from sys import stdin, setrecursionlimit
import math
from bisect import bisect_left
n = int(stdin.readline().strip())
string = stdin.readline().strip()
one = 0
zero = 0
for i in range(n):
    if string[i] == '1':
        one += 1
    else:
        zero += 1
if zero != one:
    print(1)
    print(string)
else:
    print(2)
    print(string[0], string[1:])
