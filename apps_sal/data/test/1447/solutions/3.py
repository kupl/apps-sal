import sys
n, m = list(map(int, sys.stdin.read().split()))
if m * n == 1:
    print(1)
else:
    print(1 - ((m * (n - 1)**2) / ((m * n - 1) * n)))
