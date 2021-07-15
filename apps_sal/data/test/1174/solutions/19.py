import sys
import math
import itertools
import collections
from collections import deque
import heapq 

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():

    N, M = NMI()
    A = NLI()
    
    A = list(map(lambda x: x*(-1), A))
    
    heapq.heapify(A)
    
    for m in range(M):
        highest = (heapq.heappop(A)*(-1))
        discounted = math.floor(highest/2) * -1
        heapq.heappush(A, discounted)

        
    print(sum(A)*-1)
#

def __starting_point():
    main()
__starting_point()
