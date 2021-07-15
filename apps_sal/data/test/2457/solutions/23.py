import math
import sys

#sys.stdin = open("in.txt")

t = int(input())
for i in range(t):
    n, a, b, c, d = map(int, input().split())
    a *= n
    b *= n
    a, b = a-b, a+b
    c, d = c - d, c + d
    if (d < a or b < c):
        print("No")
    else:
        print("Yes")
