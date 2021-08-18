'''input
10 4
2 3 3 1 1 2 1 2 3 3
'''
from sys import stdin
from collections import deque
import math


n, k = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))
myq = deque([])
myset = set()
for i in range(n):
    if arr[i] in myset:
        pass
    else:
        if len(myq) == k:
            el = myq[-1]
            myset.remove(el)
            myq.pop()
        myq.appendleft(arr[i])
        myset.add(arr[i])

print(len(myq))

print(*myq)
