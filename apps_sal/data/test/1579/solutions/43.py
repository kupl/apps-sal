def examA():
    N = DI()/dec(7)
    ans = N
    print(N)
    return

def examB():
    ans = 0
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    # xとyに分けるとなんか二部グラフが見えてくる
    # 違うんか。。
    def bfs(V,used,s=0):
        W = {}
        W[s] = 1
        que = deque([s])
        while(que):
            now = que.pop()
            used[now] = True
            ne = W[now]*(-1)
            for v in V[now]:
                if v not in W:
                    W[v] = ne
                    que.append(v)
                elif W[v]!=ne:
                    return False
        return W,used
    y_shift = 10**5 + 1
    N = I()
    V = defaultdict(set)
    for _ in range(N):
        x, y = LI()
        y += y_shift
        V[x].add(y)
        V[y].add(x)

    ans = 0
    used = defaultdict(lambda:False)
    for i in V.keys():
        if used[i]:
            continue
        W,used = bfs(V,used,i)
        x = 0
        for w in W.values():
            if w==1:
                x += 1
        y = len(W)-x
        #print(W,x,y)
        ans += x*y
    ans = max(0,ans-N)
    print(ans)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
nonlocal mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

def __starting_point():
    examF()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""
__starting_point()
