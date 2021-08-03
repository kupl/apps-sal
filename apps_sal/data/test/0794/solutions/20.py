from collections import deque
import sys
import math
import string
input = sys.stdin.readline
def L(): return list(map(int, input().split()))
def Ls(): return list(input().split())
def M(): return list(map(int, input().split()))


n = int(input())
l = L()
p = set(l)
if(len(p) == 1):
    print(-1)
else:
    l.sort()
    print(*l)
