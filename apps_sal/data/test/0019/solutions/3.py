from math import *

for zz in range(int(input())):
    n = int(input())
    p1, c1 = list(map(int, input().split()))
    ha = True
    if p1 < c1:
        ha = False

    for i in range(n - 1):
        p, c = list(map(int, input().split()))
        if (p - p1 < c - c1) or p < p1 or c < c1:
            ha = False
        p1 = p
        c1 = c

    if ha:
        print("YES")
    else:
        print("NO")
