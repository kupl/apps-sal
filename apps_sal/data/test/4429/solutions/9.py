from collections import defaultdict
import math as mt
import sys
import string
input = sys.stdin.readline
def L(): return list(map(int, input().split()))
def Ls(): return list(input().split())


def M(): return list(map(int, input().split()))
def I(): return int(input())


t = I()
for i in range(t):
    x, y, z = M()
    d = [x, y, z]
    p = max(x, y, z)
    c = 0
    for j in d:
        if(j == p):
            c += 1
    if(c >= 2):
        print("YES")
        if(c == 2):
            print(min(x, y, z), min(x, y, z), p)
        else:
            print(p, p, p)
    else:
        print("NO")
