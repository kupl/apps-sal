import os
import sys
from collections import defaultdict, Counter, deque
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush,heapify
from math import ceil, floor, sqrt
from copy import deepcopy


def main():
    n = int(input())
    vectoer = []
    flag = True
    for i in range(n):
        s = input()
        vectoer.append(s)

    if len(vectoer) != len(set(vectoer)):
        flag = False
        
    for i in range(n-1):
        if vectoer[i][-1] !=  vectoer[i+1][0]:
            flag = False
            break

    if flag:
        print("Yes")
    else:
        print("No")
    

def __starting_point():
	main()

__starting_point()
