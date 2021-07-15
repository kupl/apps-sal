import math,string,itertools,fractions,heapq,collections,re,array,bisect,copy
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict, deque

# Guide:
#   1. construct complex data types while reading (e.g. graph adj list)
#   2. avoid any non-necessary time/memory usage
#   3. avoid templates and write more from scratch
#   4. switch to "flat" implementations

def VI(): return list(map(int,input().split()))
def I(): return int(input())
def LIST(n,m=None): return [0]*n if m is None else [[0]*m for i in range(n)]
def ELIST(n): return [[] for i in range(n)]


def yes(A):
    print("YES")
    for l in A:
        print(" ".join([str(x) for x in l]))
def no():
    print("NO")

class FlowEdge:
    def __init__(self, v,w,capacity):
        self.v=v
        self.w=w
        self.capacity = capacity
        self.flow = 0
    def other(self, v):
        return self.w if self.v==v else self.v
    def residual_capacity_to(self, v):
        """residual capacity toward v"""
        if v == self.v:
            return self.flow
        elif v == self.w:
            return self.capacity-self.flow
        else:
            raise Exception()
    def add_residual_flow_to(self, v, delta):
        """add delta flow toward v"""
        if v == self.v:
            self.flow -= delta
        elif v == self.w:
            self.flow += delta
        else:
            raise Exception()
    def __str__(self):
        return "{}-{}: {:.0f}/{:.0f} ".format(self.v,self.w,
                                              self.flow, self.capacity)
class FlowNetwork:
    def __init__(self,nv=0):
        self.nv = nv
        self.al = ELIST(self.nv)
    def add_edge(self, e): # directed edge
        self.al[e.v].append(e)
        self.al[e.w].append(e)
    def reset(self):
        for v in self.al:
            for e in v: e.flow = 0
class FordFulkerson:
    def __init__(self,g,s,t): # graph, source, target
        self.g = g
        self.s = s
        self.t = t
        self.value = 0
        infty = 1e9
        while self.has_augmenting_path():
            bottle = infty
            v = t
            while v!=s:
                bottle = min(bottle, self.edge_to[v].residual_capacity_to(v))
                v = self.edge_to[v].other(v)
            v = t
            while v != s:
                self.edge_to[v].add_residual_flow_to(v,bottle)
                v = self.edge_to[v].other(v)
            self.value += bottle
    def has_augmenting_path(self, log=False):
        self.edge_to = [None] * self.g.nv
        self.marked = [False] * self.g.nv
        queue = deque()
        queue.append(self.s)
        self.marked[self.s] = True
        if log: i=0
        while len(queue) != 0:
            v = queue.popleft()
            for e in self.g.al[v]:
                w = e.other(v)
                if e.residual_capacity_to(w) > 0 and not self.marked[w]:
                    self.edge_to[w] = e
                    self.marked[w] = True
                    queue.append(w)
        return self.marked[self.t]


def main(info=0):
    n,m = VI()
    a = VI()
    b = VI()
    s,t = 0, 1+2*n
    fg = FlowNetwork(nv=n*2+2)
    infty = 10000000
    for i in range(n):
        fg.add_edge(FlowEdge(s,1+i,a[i]))
        fg.add_edge(FlowEdge(1+n+i,t,b[i]))
        fg.add_edge(FlowEdge(1+i,1+n+i,infty))
    for i in range(m):
        u,v = VI()
        fg.add_edge(FlowEdge(1+u-1,1+n+v-1,infty))
        fg.add_edge(FlowEdge(1+v-1,1+n+u-1,infty))

    ff = FordFulkerson(fg,s,t)
    if ff.value == sum(a) == sum(b):
        A = LIST(n,n)
        for i in range(n):
            for e in fg.al[i+1]:
                A[i][e.w-n-1] = e.flow
        yes(A)
    else:
        no()


def __starting_point():
    main()

__starting_point()
