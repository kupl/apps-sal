import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict


def main(n, s):
    if 'B' not in s:
        print(0)
        return
    b = s.count("B")
    r = s.count("R")
    op = {}
    op[0] = 1
    op[1] = 2
    op[2] = 4
    op[3] = 1 + op[2] + op[1] + op[0]
    op[3] = 8
    op[4] = 1 + op[3] + op[2] + op[1] + op[0]
    op[4] = 16
    ans = 0
    for i, x in enumerate(s):
        if x == "B":
            ans += 2**i
    print(ans)


def main_input(info=0):
    #n,p,k = map(int,input().split())
    #t = [(int(x)-1,i+1) for i,x in enumerate(input().split())]
    #l,r = list(range(n)), list(range(n))
    # for i in range(n):
    #    l[i],r[i] = map(int,input().split())
    #    t = [map(int,input().split()) for x in range(n)]
    n = int(input())
    s = input()
    main(n, s)


def __starting_point():
    main_input()


__starting_point()
