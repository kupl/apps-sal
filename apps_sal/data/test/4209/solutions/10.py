from itertools import accumulate
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
SUM = list(accumulate(A))
SUM.append(0)
BLIST = [[0] * n for i in range(n)]
B2 = []
for i in range(n):
    for j in range(i, n):
        BLIST[i][j] = SUM[j] - SUM[i - 1]
        B2.append(SUM[j] - SUM[i - 1])
B2 = sorted(set(B2))
DICT = {B2[i]: i for i in range(len(B2))}
USED = [-1] * len(B2)
ANS = [[] for i in range(len(B2))]
for i in range(n):
    for j in range(i + 1):
        x = BLIST[j][i]
        if USED[DICT[x]] < j:
            ANS[DICT[x]].append([j + 1, i + 1])
            USED[DICT[x]] = i
ANS0 = max(ANS, key=lambda x: len(x))
print(len(ANS0))
for ans in ANS0:
    print(*ans)
