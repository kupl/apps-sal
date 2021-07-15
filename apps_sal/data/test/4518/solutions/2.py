'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College

'''
from os import path
import sys
from heapq import heappush,heappop
from functools import cmp_to_key as ctk
from collections import deque,defaultdict as dd 
from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
from itertools import permutations
from datetime import datetime
from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input().rstrip()
def mi():return list(map(int,input().split()))
def li():return list(mi())
abc='abcdefghijklmnopqrstuvwxyz'
mod=1000000007
# mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]

def bo(i):
    return ord(i)-ord('a')

file = 1



    
def solve():


    

    for _ in range(ii()):

        n = ii()
        a = li()
        if len(set(a)) == 1:
            print('NO')
            continue
        print('YES')
        ans,p = [],[]
        x = a[0]
        y = -1
        for i in range(1,n):
            if a[i] != x:
                y = i+1
                ans.append([1,i+1])
            else:
                p.append(i+1)

        for i in p:
            ans.append([y,i])

        for i in ans:
            print(*i)

        















        
def __starting_point():

    if(file):

        if path.exists('input.txt'):
            sys.stdin=open('input.txt', 'r')
            sys.stdout=open('output.txt','w')
        else:
            input=sys.stdin.readline
    solve()

__starting_point()
