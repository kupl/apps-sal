from collections import deque
S = list(input())

QUE = deque()
QUE.append("START")
QUE.append("!")
ANS = 0

for s in S:
    QUE.append(s)

    while QUE[-1] == QUE[-2]:
        QUE.pop()
        QUE.pop()
        ANS += 1

if ANS % 2 == 0:
    print("No")
else:
    print("Yes")
