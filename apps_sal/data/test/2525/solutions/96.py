import sys
from collections import deque


def LS():
    return list(input().split())


S = deque(input())
Q = int(input())
rev = 0
for i in range(Q):
    A = LS()
    if A[0] == '1':
        rev += 1
        rev %= 2
    elif A[1] == '1':
        if rev == 0:
            S.appendleft(A[2])
        else:
            S.append(A[2])
    elif rev == 0:
        S.append(A[2])
    else:
        S.appendleft(A[2])
if rev == 0:
    print(''.join(S))
else:
    S.reverse()
    print(''.join(S))
