import sys

n, k = sys.stdin.readline().split()
n = int(n)
k = int(k)

a = [int(x) for x in sys.stdin.readline().split()]
b = [int(x) for x in sys.stdin.readline().split()]

MOD = (10 ** 9) + 7
res = 1

for i in range(0, n // k):
    lo = b[i] * (10 ** (k - 1)) - 1
    up = (b[i] + 1) * (10 ** (k - 1)) - 1
    tmp = (((10 ** k) - 1) // a[i]) - (up // a[i]) + (lo // a[i]) + 1
    res = res * tmp
    res = res % MOD

print(res)
