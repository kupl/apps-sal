import sys
(X, t) = map(int, sys.stdin.readline().split())
print(max(0, X - t))
