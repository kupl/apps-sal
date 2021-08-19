from collections import deque
import sys
input = sys.stdin.readline
(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
SET = set()
Q = deque()
for a in A:
    if a in SET:
        continue
    elif len(Q) == k:
        x = Q.pop()
        SET.remove(x)
        Q.appendleft(a)
        SET.add(a)
    else:
        SET.add(a)
        Q.appendleft(a)
print(len(Q))
print(*Q)
