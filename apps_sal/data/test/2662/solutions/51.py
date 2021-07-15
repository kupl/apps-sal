from collections import deque
from bisect import bisect_left
N = int(input())
A = [int(input()) for i in range(N)]

X = deque([])

for a in A:
  i = bisect_left(X,a)
  if i == 0:
    X.appendleft(a)
  else:
    X[i-1] = a
print(len(X))
