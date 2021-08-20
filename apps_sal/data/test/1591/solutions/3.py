import sys
(n, k) = list(map(int, sys.stdin.readline().strip().split()))
A = [0] * (k + 1)
for i in range(0, n):
    a = int(sys.stdin.readline().strip())
    A[a] = A[a] + 1
x = 0
y = 0
for i in range(1, k + 1):
    x = x + A[i] // 2
    y = y + A[i] % 2
print(2 * x + (y + 1) // 2)
