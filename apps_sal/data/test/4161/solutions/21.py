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
    
gcd = math.gcd

def main():
    K = I()
    ans = 0
    for i in range(1,K+1):
        for j in range(i, K+1):
            temp = gcd(i, j)
            for k in range(j, K+1):
                n = set([i,j,k])
                n = len(n)
                ans += gcd(temp,k) * (n+1)*(n)//2
    print(ans)
def __starting_point():
    main()
__starting_point()
