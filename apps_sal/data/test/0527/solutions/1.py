# coding: utf-8
# hello worldと表示する
#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
#def MXI(): return [LI() for i in range(n)]　
def SI(): return input().rstrip()
def printns(x): print(('\n'.join(x)))
def printni(x): print(('\n'.join(list(map(str,x)))))
inf = 10**17
mod = 10**9 + 7
s=SI()
t=SI()
a=len(s)
b=len(t)
#アルファベットから数字へと変換する辞書
alphasm=[chr(i) for i in range(97, 97+26)]
alphadic={}
for i in range(26):
    alphadic[alphasm[i]]=i
strlis=[[] for i in range(26)]
#print(alphadic)
#print(strlis)
for i in range(a):
    strlis[alphadic[s[i]]].append(i)
#print(strlis)
rd=0
pos=-1
#print(strlis[a])
i=0
while i<b:
    if len(strlis[alphadic[t[i]]])==0:
        print((-1))
        return
        #print("a")
    if pos==-1:
        pos=strlis[alphadic[t[i]]][0]
        i+=1
        #print("b")
    elif strlis[alphadic[t[i]]][-1]<=pos:
        rd+=1
        pos=-1
        #print("c")
    else:
        pos=strlis[alphadic[t[i]]][bisect_right(strlis[alphadic[t[i]]],pos)]
        i+=1
        #print("d")
    #print(rd,pos)
print((rd*a+pos+1))


    
        
#現在の周回数、何個目かの情報を持っておく
#次の周回に行くかどうかの判定 行かないなら二分探索




            
    

