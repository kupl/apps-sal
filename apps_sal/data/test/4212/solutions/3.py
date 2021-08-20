import sys
import itertools
(N, M, Q) = map(int, input().split())
A = []
B = []
C = []
D = []
for i in range(Q):
    (a, b, c, d) = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
num = list(range(1, M + 1))
ans = 0
for tpl in itertools.combinations_with_replacement(num, N):
    point = 0
    for i in range(Q):
        if tpl[B[i] - 1] - tpl[A[i] - 1] == C[i]:
            point += D[i]
    ans = max(ans, point)
print(ans)
