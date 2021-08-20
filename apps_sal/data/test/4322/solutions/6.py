import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
A = Counter(list(map(int, input().split())))
M = max(A)
DP0 = [0] * (M + 1)
DP1 = [0] * (M + 1)
for i in range(M + 1):
    if A[i] >= 2 and A[i - 1] >= 2:
        DP0[i] = DP0[i - 1] + A[i]
    elif A[i] >= 2 and A[i - 1] == 1:
        DP0[i] = 1 + A[i]
    elif A[i] >= 2 and A[i - 1] == 0:
        DP0[i] = A[i]
    elif A[i] == 1:
        DP0[i] = 1
    if A[i] >= 2:
        DP1[i] = DP0[i]
    elif A[i] == 1:
        DP1[i] = DP0[i - 1] + 1
ANS = max(DP1)
print(ANS)
BIG = DP1.index(ANS)
for i in range(BIG - 1, -1, -1):
    if A[i] == 1:
        SMALL = i
        break
    if A[i] == 0:
        SMALL = i + 1
        break
ANSLIST = list(range(SMALL, BIG + 1))
for i in range(BIG, SMALL - 1, -1):
    for k in range(A[i] - 1):
        ANSLIST.append(i)
print(*ANSLIST)
