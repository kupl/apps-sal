import math
from collections import deque
from sys import stdin, stdout
input = stdin.readline
for _ in range(int(input())):
    x = int(input())
    ind = 2
    mn = 99999999999999
    while ind * ind <= x:
        if x % ind == 0:
            mn = min(mn, ind)
            mn = min(mn, x // ind)
        ind += 1
    if mn == 99999999999999:
        mn = x
    print(x // mn, x - x // mn)
