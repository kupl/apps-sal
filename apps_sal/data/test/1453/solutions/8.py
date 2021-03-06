from itertools import accumulate
import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
S = list(accumulate(A))
ANS = S[:m]
for i in range(m, n):
    ANS.append(ANS[i - m] + S[i])
print(' '.join(map(str, ANS)))
