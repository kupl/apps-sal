import sys
n = int(sys.stdin.readline().strip())
a = [int(item) for item in sys.stdin.readline().strip().split()]
k = float('inf')
for i in range(n):
    if i != n - 1:
        k = min(k, int(a[i] / (n - 1 - i)))
    if i:
        k = min(k, int(a[i] / i))
print(k)
