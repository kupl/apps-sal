from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


q = deque(input())
Q = int(input())
flipped = False
for _ in range(Q):
    (q_t, *q_b) = input().split()
    if q_t == '1':
        flipped = not flipped
    else:
        (F, C) = q_b
        if F == '2' and (not flipped) or (F == '1' and flipped):
            q.append(C)
        else:
            q.appendleft(C)
q = list(q)
if flipped:
    print(''.join(q[::-1]))
else:
    print(''.join(q))
