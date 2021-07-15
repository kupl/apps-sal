# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
import sys
from sys import stdin, stdout
from collections import defaultdict
from collections import deque
import math
import copy

#T = int(input())
#N = int(input())
#s1 = input()
#s2 = input()
N,E = [int(x) for x in stdin.readline().split()]
#arr = [int(x) for x in stdin.readline().split()]

s = 0
size = [1]*N

f = [x for x in range(N)]

def getf(v):
    stack = []
    while f[v] != v:
       stack.append(v)
       v = f[v]
    for idx in stack:
        f[idx] = v
    return v

def merge(f, v, u):
    nonlocal s
    t1 = getf(v)
    t2 = getf(u)
    if t1 != t2:
        A = size[t1]
        B = size[t2]
        s -= A*(A-1)//2
        s -= B*(B-1)//2
        size[t1] = size[t1] + size[t2]
        C = size[t1]
        s += C*(C-1)//2
        f[t2] = t1


w_edge = {}
for i in range(N-1):
    u,v,w = [int(x) for x in stdin.readline().split()]
    if u>v:
        u,v = v,u

    if w not in w_edge:
        w_edge[w] = []

    w_edge[w].append((u,v))

q = [0]*200000
for i in range(200000):
    if i+1 in w_edge:
        for e in w_edge[i+1]:
            u,v = e
            merge(f,u-1,v-1)
        q[i] = s
    else:
        if i!=0:
            q[i] = q[i-1]
        else:
            q[i] = 0

arr = [int(x) for x in stdin.readline().split()]
ans = [0]*E
for i in range(E):
    ans[i] = q[arr[i]-1]

print(*ans)

