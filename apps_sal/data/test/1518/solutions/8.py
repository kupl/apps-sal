import math
import bisect
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    A[i] -= 1

x = 10**5
L = math.floor(math.sqrt(x))  # 平方根を求める

Primelist = [i for i in range(x + 1)]
Primelist[1] = 0  # 1は素数でないので0にする.

for i in Primelist:
    if i > L:
        break
    if i == 0:
        continue
    for j in range(2 * i, x + 1, i):
        Primelist[j] = 0

Primes = [Primelist[j] - 1 for j in range(x + 1) if Primelist[j] != 0]

A_INV = [-1] * n
for i in range(n):
    A_INV[A[i]] = i

ANS = []
for i in range(n):

    j = A_INV[i]

    while j - i:
        t = bisect.bisect(Primes, j - i) - 1
        sa = Primes[t]

        ANS.append((j - sa, j))

        A_INV[i], A_INV[A[j - sa]] = j - sa, j
        A[j], A[j - sa] = A[j - sa], A[j]

        j -= sa

print(len(ANS))
for x, y in ANS:
    print(x + 1, y + 1)
