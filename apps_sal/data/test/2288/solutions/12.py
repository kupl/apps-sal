from collections import deque
from sys import stdin, stdout
import math
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    types = list(map(int, input().split()))
    if types.count(1) and types.count(0):
        print('Yes')
    else:
        if sorted(arr) == arr:
            print('Yes')
        else:
            print('No')
