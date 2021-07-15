ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
import sys
ceil = math.ceil
gcd = math.gcd
RL = sys.stdin.readline
INF=10**15
def ceilab(a,b):
    return (a+b-1)//b
def JK(s1,s2):
    if s1=="R":
        if s2=="P":
            return s2
        else:
            return s1
    elif s1=="S":
        if s2=="R":
            return s2
        else:
            return s1
    elif s1=="P":
        if s2=="S":
            return s2
        else:
            return s1

N,K=ma()
S = list(input())
S = S*2
T=[]
for k in range(K):
    T=[]
    for i in range(N):
        T.append(JK(S[2*i],S[2*i+1]))
    S = T*2
print(T[0])

