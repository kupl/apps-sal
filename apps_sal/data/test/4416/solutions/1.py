from itertools import accumulate
import sys
input = sys.stdin.readline
(n, k) = list(map(int, input().split()))
BOOKS = [tuple(map(int, input().split())) for i in range(n)]
A = []
B = []
AB = []
for (t, a, b) in BOOKS:
    if a == 1 and b == 1:
        AB.append(t)
    if a == 1 and b == 0:
        A.append(t)
    if a == 0 and b == 1:
        B.append(t)
A.sort()
B.sort()
AB.sort()
SA = [0] + list(accumulate(A))
SB = [0] + list(accumulate(B))
SAB = [0] + list(accumulate(AB))
ANS = 1 << 31
for i in range(len(SAB)):
    if 0 <= k - i < len(SA) and 0 <= k - i < len(SB):
        ANS = min(ANS, SAB[i] + SA[k - i] + SB[k - i])
if ANS == 1 << 31:
    print(-1)
else:
    print(ANS)
