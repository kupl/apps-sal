import sys
import math


def inint(): return int(sys.stdin.readline())
def inintm(): return list(map(int, sys.stdin.readline().split()))
def inintl(): return list(inintm())
def instrm(): return list(map(str, sys.stdin.readline().split()))
def instrl(): return list(instrm())


n = inint()
X = inintl()

X_sorted = sorted(X)

a, b = X_sorted[n // 2 - 1], X_sorted[n // 2]

for x in X:
    if x <= a:
        print(b)
    else:
        print(a)
