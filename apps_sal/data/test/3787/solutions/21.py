def examC():
    N = LI(); N.sort()
    if N[0]==1:
        if N[1]==1:
            ans = 1
        else:
            ans = max(0,N[1]-2)
    else:
        ans = (N[1]-2)*(N[0]-2)
    print(ans)
    return

def examD():
    N, K = LI()
    ans = 0
    b = K+1
    while(b<=N):
        cur = N//b * (b-K) + max(0,N%b - K+1)
        if cur==N+1:
            cur = N
        ans += cur
        b += 1
#        print(ans)
    print(ans)
    return

def examE():
    N, A, B = LI()
    if N<A+B-1 or N>A*B:
        print(-1)
        return
    ans = []
    cur = N
    num = N
    rest = B - 1
    #print(rest)
    for i in range(B):
        cur -= A
        if cur<=rest:
            cur += A
            break
        for j in range(A):
            if num==rest:
                break
            ans.append(cur+1)
            cur += 1
            num -= 1
        cur -= A
        rest -= 1
    for i in range(rest,cur):
        ans.append(i+1)
    cur = rest
    for j in range(rest):
        ans.append(cur)
        cur -= 1
    print(" ".join(map(str,ans)))
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
nonlocal mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

def __starting_point():
    examE()

"""

"""
__starting_point()
