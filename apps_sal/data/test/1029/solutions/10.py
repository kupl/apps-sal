import sys
from math import *
from collections import *


def readints():
    return list(map(int, input().strip('\n').split()))


s = input()
n = len(s)
arr = deque()
i = n - 1
while i >= 0:
    j = i
    while j >= 0 and s[j] == '0':
        j -= 1
    arr.appendleft(((j, i), 1))
    i = j - 1


def gte(x, y):
    if x[1] - x[0] > y[1] - y[0]:
        return True
    if x[1] - x[0] < y[1] - y[0]:
        return False
    n = x[1] - x[0] + 1
    for i in range(n):
        if s[i + x[0]] > s[i + y[0]]:
            return True
        if s[i + x[0]] < s[i + y[0]]:
            return False
    return True


while len(arr) > 1:
    x = arr.popleft()
    y = arr.popleft()
    if gte(x[0], y[0]):
        arr.appendleft(((x[0][0], y[0][1]), x[1] + y[1]))
    else:
        arr.appendleft(((x[0][0], y[0][1]), 1))
print(arr[0][1])
