from collections import *
from sys import setrecursionlimit, stdin
import threading

mod = 1000000007


def arr_inp(n):
    if n == 1:
        return [int(x) for x in stdin.readline().split()]
    elif n == 2:
        return [float(x) for x in stdin.readline().split()]
    else:
        return list(stdin.readline()[:-1])


def main():
    class graph:
        def __init__(self, gdict=None):
            if gdict is None:
                gdict = defaultdict(list)
            self.gdict, self.edges, self.l = gdict, [], defaultdict(int)

        def addEdge(self, node1, node2, w=None):
            self.gdict[node1].append(node2)

        def scc_utils(self, v):

            self.disc[v], self.low[v], self.stack[v] = self.time, self.time, 1
            self.time += 1
            self.st.append(v)

            for i in self.gdict[v]:
                if self.disc[i] == -1:
                    self.scc_utils(i)
                    self.low[v] = min(self.low[v], self.low[i])

                elif self.stack[i]:
                    self.low[v] = min(self.low[v], self.disc[i])

            if self.low[v] == self.disc[v]:
                node, mem = -1, defaultdict(int)
                while node != v:
                    node = self.st.pop()
                    self.stack[node] = 0
                    mem[cost[node - 1]] += 1

                self.count += min(mem)
                self.mi = ((self.mi % mod) * (mem[min(mem)] % mod)) % mod

        def scc(self, n):
            self.time, self.count, self.mi = 0, 0, 1
            self.disc, self.low, self.stack, self.st = [-1] * (n + 1), [-1] * (n + 1), [0] * (n + 1), []
            for i in range(1, n + 1):
                if self.disc[i] == -1:
                    self.scc_utils(i)

            print(self.count, self.mi)

    n, cost, m, g = int(input()), arr_inp(1), int(input()), graph()
    for i in range(m):
        u, v = arr_inp(1)
        g.addEdge(u, v)
    g.scc(n)


def __starting_point():
    setrecursionlimit(80000)
    threading.stack_size(102400000)
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
