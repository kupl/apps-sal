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
    N, M = MI()
    L = set([I() for i in range(M)])
    mod = 1000000007
    D = [0]*(N+2)
    D[1]=1
    
    for i in range(1, N+1):
        if not i in L:
            D[i+1] = (D[i]+D[i-1]) % mod

    print(D[N+1]%mod)
    
    
def __starting_point():
    main()
__starting_point()
