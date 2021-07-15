import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
import bisect
import re
from collections import Counter,deque,defaultdict
def iinput(): return int(input())
def imap(): return map(int, input().split())
def ilist(): return list(imap())
def irow(N): return [iinput() for i in range(N)]
def sinput(): return input().rstrip()
def smap(): return sinput().split()
def slist(): return list(smap())
def srow(N): return [sinput() for i in range(N)]

def main():
    n = iinput()
    s = sorted(ilist())[::2]
    print(sum(s))



def __starting_point():
    main()
__starting_point()
