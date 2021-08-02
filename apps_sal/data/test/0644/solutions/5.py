import sys
from collections import deque
input = sys.stdin.readline

l = int(input())

QUE = deque()

for q in range(l):
    QUE.append(input().split())

    while len(QUE) >= 2 and QUE[-1][0] == "end" and QUE[-2][0] == "for":
        QUE.pop()
        QUE.pop()


ANS = 0
Q = deque()
Q.append(1)
SUM = 1

for s in QUE:

    if s[0] == "add":
        ANS += SUM
    elif s[0] == "for":
        Q.append(int(s[1]))
        SUM = min(SUM * int(s[1]), 1 << 40)

    else:
        x = Q.pop()
        SUM //= x

    if ANS > 2**32 - 1:
        print("OVERFLOW!!!")
        break

else:
    print(ANS)
