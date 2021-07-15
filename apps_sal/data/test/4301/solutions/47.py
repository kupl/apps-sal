import sys
import math
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
    N = I()
    L = [I() for i in range(N)]
    L2=sorted(L)
    max_n = L2[N-1]
    max_n2 = L2[N-2]
    if max_n==max_n2:
        for i in range(N):
            print(max_n)
    else:
        for i in L:
            if i != max_n:
                print(max_n)
            else:
                print(max_n2)
            

        
    
    
def __starting_point():
    main()
__starting_point()
