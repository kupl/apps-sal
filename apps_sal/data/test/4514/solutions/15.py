from collections import *
from sys import stdin
from bisect import *


def arr_inp(n):
    if n == 1:
        return [int(x) for x in stdin.readline().split()]
    elif n == 2:
        return [float(x) for x in stdin.readline().split()]
    else:
        return [str(x) for x in stdin.readline().split()]


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = defaultdict(list)
        self.gdict = gdict

    def add_edge(self, node1, node2):
        self.gdict[node1].append(node2)

    def dfsUtil(self, v):
        stack, self.visit, out = [v], [0] * (n + 1), []

        while (stack):
            s = stack.pop()

            if not self.visit[s]:
                out.append(s)
                self.visit[s] = 1

            for i in sorted(self.gdict[s], reverse=True):
                if not self.visit[i]:
                    stack.append(i)

        return out


n, q = arr_inp(1)
p, g, mem, quary = arr_inp(1), graph(), [1 for i in range(n + 1)], defaultdict(lambda: -1)

for i in range(2, n + 1):
    g.add_edge(p[i - 2], i)

all, ans = g.dfsUtil(1), []
mem2 = {all[i]: i for i in range(n)}

for i in all[::-1]:
    for j in g.gdict[i]:
        mem[i] += mem[j]


for i in range(q):
    u, v = arr_inp(1)
    ans.append(str(-1 if mem[u] < v else all[mem2[u] + v - 1]))

print('\n'.join(ans))
