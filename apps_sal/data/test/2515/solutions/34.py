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
def MI(): return list(map(int, input().split()))
def MF(): return list(map(float,input().split()))
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]

def Eratosthenes(n):
    from math import sqrt
    res = [True] * (n+1)
    res[0] = False
    res[1] = False
    
    for i in range(2,int(sqrt(n))+1):
        if res[i]:
            for j in range(2*i,n+1,i):
                res[j] = False
    return res

class BIT():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n+1)

    #bit_indexにxをO(log(n))で加算する
    def add(self,i,x):
        #if(i<=0 or i>n):return iに0以下の数字は代入しない
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)
    #bit_1 + bit_2 + …  + bit_n をO(log(n))で求める
    def sum(self,i):
        s = 0
        #iに0以下の数字は代入しない。
        while i > 0:
            s+=self.bit[i]
            i -= (i & -i)
        return s
    
    def rangesum(self,i,k):
        return self.sum(k) - self.sum(i)
    #a_1 + a_2 + … + a_i >= x となるような最小のiを求める(a_k >= 0)
    #xが0以下の場合は該当するものなし→0を返す
    def lower_bound(self,x):
        if x <= 0:
            return 0
        else:
            i = 0
            r = 1
            #最大としてありうる区間の長さを取得する
            #n以下の最小の二乗のべき(BITで管理する数列の区間で最大のもの)を求める
            while(r<self.n):
                r=r<<1
            len = r
            while len > 0:
                if(i+len<self.n and self.bit[i+len]<x):
                    x-=self.bit[i+len]
                    i+=len
                len = len >> 1
            return i+1

def main():
    max_num = 100000
    Q = I()
    S = Eratosthenes(max_num)
    bit = BIT(max_num)
    
    #bitの初期化
    for a in range(1,max_num, 2):
        b = (a+1) // 2
        if S[a] and S[b]:
            bit.add(a, 1)
    
    #queryの処理
    
    for q in range(Q):
        l, r = MI()
        print((bit.sum(r)-bit.sum(l-1)))

def __starting_point():
    main()

__starting_point()
