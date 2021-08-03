from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

A2 = [A[i] % 2 for i in range(n)]

if n == 1:
    print("YES")
    return

if n == 2:
    if A2[0] != A2[1]:
        print("NO")
        return
    else:
        print("YES")
        return

QUE = deque()

for i in range(n):
    QUE.append(A2[i])

    while len(QUE) >= 2 and QUE[-1] == QUE[-2]:
        QUE.pop()
        QUE.pop()

if len(QUE) >= 2:
    print("NO")
else:
    print("YES")
