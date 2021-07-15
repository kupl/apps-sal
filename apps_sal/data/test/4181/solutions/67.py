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
    L = LI()
    L2 = LI()
    ans = 0
    for index, num in enumerate(L2):
        if L[index] >= num:
            ans+=num
            L[index]-=num
        else:
            if L[index]+L[index+1] >= num:
                ans+=num
                L[index+1] -= num-L[index]
                L[index] = 0
            else:
                ans += L[index]+L[index+1]
                L[index] = 0
                L[index+1] = 0
    print(ans)
        
    
def __starting_point():
    main()
__starting_point()
