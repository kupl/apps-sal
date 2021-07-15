import sys

A, B = map(int, sys.stdin.readline().split())
if A <= 5:
    print(0)
elif A <= 12:
    print(B // 2)
else:
    print(B)
