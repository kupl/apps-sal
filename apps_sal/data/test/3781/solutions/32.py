import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
from collections import deque, defaultdict, Counter
import heapq
from functools import reduce
from itertools import permutations
import math
import bisect

def main():
    T = I()
    for i in range(T):
        N = I()
        A = LI()
        if N % 2 == 1:
            print('Second')
        else:
            D = defaultdict(int)
            for a in A:
                D[a] += 1
            flag = 0
            for key in list(D.keys()):
                if D[key] % 2 != 0:
                    flag = 1
                    break
            if flag == 0:
                print('Second')
            else:
                print('First')
def __starting_point():
    main()

__starting_point()
