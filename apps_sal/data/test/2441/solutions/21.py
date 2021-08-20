from collections import *
from sys import setrecursionlimit, stdin
import threading
from types import GeneratorType


def bootstrap(f, stack=[]):

    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


mod = 1000000007


def rints():
    return [int(x) for x in stdin.readline().split()]


class graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = defaultdict(list)
        (self.gdict, self.edges, self.l) = (gdict, [], defaultdict(int))

    def addEdge(self, node1, node2, w=None):
        self.gdict[node1].append(node2)

    @bootstrap
    def scc_utils(self, v):
        (self.disc[v], self.low[v], self.stack[v]) = (self.time, self.time, 1)
        self.time += 1
        self.st.append(v)
        for i in self.gdict[v]:
            if self.disc[i] == -1:
                yield self.scc_utils(i)
                self.low[v] = min(self.low[v], self.low[i])
            elif self.stack[i]:
                self.low[v] = min(self.low[v], self.disc[i])
        if self.low[v] == self.disc[v]:
            (node, mem) = (-1, defaultdict(int))
            while node != v:
                node = self.st.pop()
                self.stack[node] = 0
                mem[cost[node - 1]] += 1
            self.count += min(mem)
            self.mi = self.mi % mod * (mem[min(mem)] % mod) % mod
        yield

    def scc(self, n):
        (self.time, self.count, self.mi) = (0, 0, 1)
        (self.disc, self.low, self.stack, self.st) = ([-1] * (n + 1), [-1] * (n + 1), [0] * (n + 1), [])
        for i in range(1, n + 1):
            if self.disc[i] == -1:
                self.scc_utils(i)
        print(self.count, self.mi)


(n, cost, m, g) = (int(input()), rints(), int(input()), graph())
for i in range(m):
    (u, v) = rints()
    g.addEdge(u, v)
g.scc(n)
