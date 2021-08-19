import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
import sys
letters = ascii_letters
input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    can = list(map(int, input().split()))
    vals = sorted([i for i in range(n) if not can[i]], key=lambda x: -arr[x])
    res = [0] * n
    last = 0
    for i in range(n):
        if can[i]:
            res[i] = arr[i]
        else:
            res[i] = arr[vals[last]]
            last += 1
    print(*res)
