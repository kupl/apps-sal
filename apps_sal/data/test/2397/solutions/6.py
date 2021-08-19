import sys
(n, k) = list(map(int, sys.stdin.readline().strip().split()))
a = list(map(int, sys.stdin.readline().strip().split()))
L = [a[-1]] * n
for i in range(1, n):
    L[i] = L[i - 1] + a[n - i - 1]
x = L.pop()
L.sort()
for i in range(0, k - 1):
    x = x + L[n - 2 - i]
print(x)
