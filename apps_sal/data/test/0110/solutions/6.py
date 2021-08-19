import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
for i in range(0, n):
    if a[i] >= 0:
        a[i] = -a[i] - 1
if n % 2 == 1:
    i = a.index(min(a))
    a[i] = -a[i] - 1
a = list(map(str, a))
print(' '.join(a))
