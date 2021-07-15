import sys

n = int(sys.stdin.readline().strip())
a = sys.stdin.readline().strip().split()
k = len(str(a[0]))
A = [0] * k
for i in range (0, n):
    for j in range (0, k):
        A[j] = A[j] + int(a[i][j])
s = 0
for j in range (0, k):
    s = (s + 11 * (100**(k-j-1)) * A[j]) % 998244353
print((s * n) % 998244353)
