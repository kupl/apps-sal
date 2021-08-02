import sys
import math
import fractions
import heapq
import copy
from collections import defaultdict
stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))


class My_heapavi():
    def __init__(self):
        self.p = list()
        self.q = list()
        self.p2 = list()
        self.q2 = list()

    def insert(self, x):
        heapq.heappush(self.p, x)
        heapq.heappush(self.p2, -x)
        return

    def erase(self, x):
        heapq.heappush(self.q, x)
        heapq.heappush(self.q2, -x)
        return

    def minimum(self):
        while self.q and self.p[0] == self.q[0]:
            heapq.heappop(self.p)
            heapq.heappop(self.q)
        return self.p[0]

    def maximum(self):
        while self.q2 and self.p2[0] == self.q2[0]:
            heapq.heappop(self.p2)
            heapq.heappop(self.q2)
        return -self.p2[0]

    def size(self):
        return len(self.p) - len(self.q)


s = [My_heapavi() for i in range(200005)]
maxs = My_heapavi()


def getmax(i):
    if(s[i].size() == 0):
        return -1
    return s[i].maximum()


def addYouchien(i):
    x = getmax(i)
    if(x == -1):
        return
    maxs.insert(x)


def delYouchien(i):
    x = getmax(i)
    if(x == -1):
        return
    maxs.erase(x)


def addEnji(i, x):
    delYouchien(i)
    s[i].insert(x)
    addYouchien(i)


def delEnji(i, x):
    delYouchien(i)
    s[i].erase(x)
    addYouchien(i)


N, Q = nm()
a = [0 for i in range(200005)]
b = [0 for i in range(200005)]

for i in range(N):
    a[i], b[i] = nm()
    addEnji(b[i], a[i])

for i in range(Q):
    c, d = nm()
    c -= 1
    delEnji(b[c], a[c])
    b[c] = d
    addEnji(b[c], a[c])
    print(maxs.minimum())
