import sys
input = sys.stdin.readline
from collections import deque

K = int(input())

D = [-1]*K

q = deque()
q.append(1)
D[1] = 1
while q:
    p = q.pop()
    n1 = (p*10)%K
    if D[n1] == -1 or D[n1] > D[p]:
        D[n1] = D[p]
        q.append(n1)
    n2 = (p+1)%K
    if D[n2] == -1:
        D[n2] = D[p] + 1
        q.appendleft(n2)
print(D[0])
