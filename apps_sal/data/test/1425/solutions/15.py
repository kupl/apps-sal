"""input
4
1 10 100 1000
"""
from sys import stdin, setrecursionlimit
import math
from bisect import bisect_left
from collections import deque


def check(circle):
    for i in range(len(circle)):
        if i == 0:
            left = circle[-1]
        else:
            left = circle[i - 1]
        if i == len(circle) - 1:
            right = circle[0]
        else:
            right = circle[i + 1]
        if left + right <= circle[i]:
            return False
    return True


n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
arr.sort()
circle = []
circle = deque(circle)
circle.append(arr[0])
flag = 0
for i in range(1, n):
    if flag == 0:
        circle.append(arr[i])
        flag = 1
    else:
        circle.appendleft(arr[i])
        flag = 0
circle = list(circle)
if check(circle):
    print('YES')
    print(*circle)
else:
    print('NO')
