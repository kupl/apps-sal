import sys


fin = sys.stdin


[n, m] = [int(x) for x in fin.readline().split()]


left = m - 1
right = n - m

if left >= right:
    print(max(m - 1, 1))
else:
    print(min(m + 1, n))
