import sys
fin = sys.stdin
M = 1000000007


def egcd(a, b):
    d = a
    if b != 0:
        d, y, x = egcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    else:
        return a, 1, 0


def inv(a, m):
    d, x, y = egcd(a, m)
    return (m + x % m) % m


a = fin.readline().strip()
k = int(fin.readline())
n = len(a)
D = (inv(pow(2, n, M) - 1, M) * (pow(2, n * k, M) - 1)) % M
S = 0
for i in range(n):
    if a[i] in ['0', '5']:
        S = (S + pow(2, i, M)) % M
print((D * S) % M)
