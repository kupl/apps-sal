from bisect import bisect_left
from collections import deque

n = int(input())
A = [int(input()) for _ in range(n)]

D = deque([])

for a in A:
    i = bisect_left(D, a)
    if i == 0:
        D.appendleft(a)
    else:
        D[i - 1] = a

print(len(D))
