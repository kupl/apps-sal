import sys
(A, B) = map(int, sys.stdin.readline().split())
print((B - A - 1) // (A - 1) + 2)
