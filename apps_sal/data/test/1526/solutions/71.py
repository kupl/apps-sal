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
    A, B, C = MI()
    a = min(A,B,C)
    c = max(A,B,C)
    b = A+B+C-a-c
    ans = 0
    if (b-a)%2 == 1:
        a+=1
        c+=1
        ans += 1
    ans += (b-a)//2
    ans += (c-b)
    print(ans)

def __starting_point():
    main()
__starting_point()
