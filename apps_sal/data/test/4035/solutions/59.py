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
    A, B = MI()
    B1 = B * 10
    
    while True:
        if B1 * 0.1 >= B+1:
            break
        elif B1 * 0.08 >= A+1:
            break
        elif math.floor(B1 * 0.08) == A:
            print(B1)
            return
            
        
        
        
        B1 += 1

        
    
    print(-1)
    
def __starting_point():
    main()
__starting_point()
