import sys
import math
import itertools
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]

def main():
    N = input().rstrip()
    keta = len(N)
    N = int(N)
    A = ["3", "5", "7"]
    res = 0
    for i in itertools.product(A, repeat=keta):
        if len(set(i)) <= 2:
            pass
        else:
            temp = "".join(i)
            if int(temp) <= N:
                res += 1

    while keta >= 2:
        res+= pow(3, keta-1) - 3 * pow(2, keta-1) + 3
        keta-=1

    print(res)
    
def __starting_point():
    main()
__starting_point()
