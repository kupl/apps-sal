from collections import deque
n = int(input())
S = input()

QUE = deque(S)
ANS = []

while QUE:
    if len(QUE) == 1:
        QUE.pop()
        break
    if QUE[0] == QUE[1]:
        QUE.popleft()
    elif QUE[0] != QUE[1]:
        x = QUE.popleft()
        y = QUE.popleft()
        ANS.append(x)
        ANS.append(y)

print(n - len(ANS))
print("".join(ANS))
