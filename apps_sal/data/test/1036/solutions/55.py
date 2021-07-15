from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

win = [('R','S'),('S','P'),('P','R')]
def ch(a,b):
    if a == b: return True
    if (a,b) in win: return True
    return False
n,k = inpl()
s = list(input())
for _ in range(k):
    s += s
    nx = []
    for i in range(2*n)[::2]:
        if ch(s[i],s[i+1]): nx.append(s[i])
        else: nx.append(s[i+1])
    s = nx[::]
print(s[0])
