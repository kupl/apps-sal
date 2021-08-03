import math
import sys


MAX_N = 500


N = int(input())
C = []
S = []
F = []
for _ in range(N - 1):
    c, s, f = [int(x) for x in input().split()]
    C.append(c)
    S.append(s)
    F.append(f)

if N == 1:
    print((0))
    return

for i in range(N - 1):
    t = S[i] + C[i]
    for j in range(i + 1, N - 1):
        t = max(S[j], int(math.ceil(t / F[j])) * F[j]) + C[j]
    print(t)
print((0))
