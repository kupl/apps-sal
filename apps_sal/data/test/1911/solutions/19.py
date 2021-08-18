import sys

n, k = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))

d = []
for i in range(1, n):
    d.append(a[i] - a[i - 1])
d.sort()
print(sum(d[:n - k]))
