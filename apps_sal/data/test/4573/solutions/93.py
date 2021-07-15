import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: list(map(int, sys.stdin.readline().split()))
inintl = lambda: list(inintm())
instrm = lambda: list(map(str, sys.stdin.readline().split()))
instrl = lambda: list(instrm())


n = inint()
X = inintl()

X_sorted = sorted(X)

a, b = X_sorted[n//2-1],X_sorted[n//2]

for x in X:
    if x <= a:
        print(b)
    else:
        print(a)

