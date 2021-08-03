import math as ma
# import sys
# input=sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 4 == 0:
        print("YES")
    else:
        print("NO")
