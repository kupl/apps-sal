# coding: utf-8
import math
from collections import deque
n = int(input())
#x, y = map(int,input().split())
A = list(map(int, input().split()))
ans = 0
B = deque()
if n % 2 == 0:
    for i in range(n):
        a = str(A[i])
        if i % 2 == 1:
            B.appendleft(a)
        else:
            B.append(a)
if n % 2 == 1:
    for i in range(n):
        a = str(A[i])
        if i % 2 == 0:
            B.appendleft(a)
        else:
            B.append(a)
print(' '.join(B))
