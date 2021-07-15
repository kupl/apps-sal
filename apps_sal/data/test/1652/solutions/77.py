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
    word = ["dream", "dreamer","erase", "eraser"]
    word = [i[::-1] for i in word]
    S = input().rstrip()
    S = S[::-1]

    while True:
        length = len(S)
        for w in word:
            length2 = len(w)
            if length >= length2 and S[0:length2] == w:
                S = S[length2:length]
        if len(S) == length:
            break
    if len(S) == 0:
        print("YES")
    else:
        print("NO")

    
def __starting_point():
    main()
__starting_point()
