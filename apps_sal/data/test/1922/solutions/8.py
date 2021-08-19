import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
if n == m == 1:
    print(1)
elif min(n, m) == 1:
    print(max(n, m) - 2)
else:
    print((n - 2) * (m - 2))
