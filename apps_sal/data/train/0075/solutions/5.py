# cook your dish here
# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

import math
import collections
from sys import stdin, stdout, setrecursionlimit
import bisect as bs
T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    # a,b,c,d = list(map(int,stdin.readline().split()))
    # h = list(map(int,stdin.readline().split()))
    # b = list(map(int,stdin.readline().split()))
    # a = stdin.readline().strip('\n')
    t = 2 * n
    x = math.pi / (2 * t)
    h = 0.5 / (math.sin(x))
    print(round(h, 7))
