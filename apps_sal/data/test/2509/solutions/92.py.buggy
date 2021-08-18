import sys

n, k = list(map(int, input().split()))

if k == 0:
    print((n * n))
    return

icnt = 0
for ki in range(k + 1, n + 1):
    qki = n // ki
    icnt += qki * (ki - k) + max(n % ki - (k - 1), 0)

print(icnt)
