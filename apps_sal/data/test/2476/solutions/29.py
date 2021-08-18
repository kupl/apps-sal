from collections import Counter
from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

B = list(Counter(A).values())

C = [0] * N
for i in B:
    C[i - 1] += 1

F = list(accumulate(C))

S = [0] * N
f = [0] * N
S[0] = f[0] = sum(C)
for i in range(2, N + 1):
    S[i - 1] = (S[i - 2] + C[i - 1] + S[0] - F[i - 1])
    f[i - 1] = S[i - 1] / i

f.sort()
n = 0
K = 1

while K != N + 1:
    if K <= f[n]:
        print(N - n)
        K += 1
    else:
        n += 1
    if n == N:
        for i in range(N - K + 1):
            print(0)
        K = N + 1
