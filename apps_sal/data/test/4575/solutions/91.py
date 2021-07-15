import sys
from collections import deque
#import numpy as np
import math
#sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def solve():
    return

def __starting_point():
    n = I()
    d,x = IL()
    days = 0
    for _ in range(n):
        a = I()
        tmp = 1
        count = 1
        while tmp<=d:
            days += 1
            tmp = count*a + 1
            count += 1
    ans = days + x
    print(ans)
    solve()
__starting_point()
