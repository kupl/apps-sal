import os
import sys
from io import BytesIO, IOBase
# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline()
 
# ------------------------------


def RL(): return map(int, sys.stdin.readline().split())
def RLL(): return list(map(int, sys.stdin.readline().split()))
def N(): return int(input())
def print_list(l):
    print(' '.join(map(str,l)))
# sys.setrecursionlimit(100000)
# from heapq import *
# from collections import deque as dq
# from math import ceil,floor,sqrt,pow,gcd,log
# import bisect as bs
# from collections import Counter
from collections import defaultdict as dc 
# from functools import lru_cache
n,k = RL()
dic = [[] for _ in range(1000)]
for _ in range(n):
    page = N()
    for _ in range(k):
        dic[page].append(input().strip())
dic = [word for page in dic for word in page]
nw = len(dic)
# print(dic)
ingress = dc(int)
edges = dc(list)
chars = set()
chars|=set(dic[0])
F = True
for i in range(1,nw):
    a,b = dic[i-1],dic[i]
    if len(chars)<26: chars|=set(b)
    flag = False
    for i,j in zip(a,b):
        if i!=j:
            ingress[j]+=1
            edges[i].append(j)
            flag = True
            break
    if not flag and len(b)<len(a):
        F = False
        break
if not F:
    print('IMPOSSIBLE')
else:
# print(edges)
    res = ''
    now = []
    for c in chars:
        ingress[c] = max(0,ingress[c])
        if ingress[c]==0:
            now.append(c)
    # print(ingress)
    while now:
        a = now.pop()
        res+=a 
        for b in edges[a]:
            ingress[b]-=1
            if ingress[b]==0:
                now.append(b)

    if len(res)==len(chars):
        print(res)
    else:
        print('IMPOSSIBLE')
