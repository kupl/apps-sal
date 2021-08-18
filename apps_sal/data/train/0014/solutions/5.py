import sys
import bisect
import string
import math
import time
import functools
import random
from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, groupby
def Golf(): *a, = map(int, open(0))
def I(): return int(input())
def S_(): return input()
def IS(): return input().split()
def LS(): return [i for i in input().split()]
def LI(): return [int(i) for i in input().split()]
def LI_(): return [int(i) - 1 for i in input().split()]
def NI(n): return [int(input()) for i in range(n)]
def NI_(n): return [int(input()) - 1 for i in range(n)]
def StoLI(): return [ord(i) - 97 for i in input()]
def ItoS(n): return chr(n + 97)
def LtoS(ls): return ''.join([chr(i + 97) for i in ls])


def GI(V, E, ls=None, Directed=False, index=1):
    org_inp = []
    g = [[] for i in range(V)]
    FromStdin = True if ls == None else False
    for i in range(E):
        if FromStdin:
            inp = LI()
            org_inp.append(inp)
        else:
            inp = ls[i]
        if len(inp) == 2:
            a, b = inp
            c = 1
        else:
            a, b, c = inp
        if index == 1:
            a -= 1
            b -= 1
        aa = (a, c)
        bb = (b, c)
        g[a].append(bb)
        if not Directed:
            g[b].append(aa)
    return g, org_inp


def GGI(h, w, search=None, replacement_of_found='.', mp_def={'
    mp=[boundary] * (w + 2)
    found={}
    for i in range(h):
        s = input()
        for char in search:
            if char in s:
                found[char] = ((i + 1) * (w + 2) + s.index(char) + 1)
                mp_def[char] = mp_def[replacement_of_found]
        mp += [boundary] + [mp_def[j] for j in s] + [boundary]
    mp += [boundary] * (w + 2)
    return h + 2, w + 2, mp, found


def TI(n): return GI(n, n - 1)


def bit_combination(k, n=2):
    rt = []
    for tb in range(n**k):
        s = [tb // (n**bt) % n for bt in range(k)]
        rt += [s]
    return rt


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['YES', 'NO']
Yn = ['Yes', 'No']
mo = 10**9 + 7
inf = float('inf')
l_alp = string.ascii_lowercase
def input(): return sys.stdin.readline().rstrip()


class Tree:
    def __init__(self, inp_size=None, init=True):
        self.LCA_init_stat = False
        self.ETtable = []
        if init:
            self.stdin(inp_size)
        return

    def stdin(self, inp_size=None, index=1):
        if inp_size == None:
            self.size = int(input())
        else:
            self.size = inp_size
        self.edges, _=GI(self.size, self.size - 1, index=index)
        return

    def listin(self, ls, index=0):
        self.size = len(ls) + 1
        self.edges, _=GI(self.size, self.size - 1, ls, index=index)
        return

    def __str__(self):
        return str(self.edges)

    def dfs(self, x, func=lambda prv, nx, dist: prv + dist, root_v=0):
        q = deque()
        q.append(x)
        v = [-1] * self.size
        v[x] = root_v
        while q:
            c = q.pop()
            for nb, d in self.edges[c]:
                if v[nb] == -1:
                    q.append(nb)
                    v[nb] = func(v[c], nb, d)
        return v

    def EulerTour(self, x):
        q = deque()
        q.append(x)
        self.depth = [None] * self.size
        self.depth[x] = 0
        self.ETtable = []
        self.ETdepth = []
        self.ETin = [-1] * self.size
        self.ETout = [-1] * self.size
        cnt = 0
        while q:
            c = q.pop()
            if c < 0:
                ce = ~c
            else:
                ce = c
                for nb, d in self.edges[ce]:
                    if self.depth[nb] == None:
                        q.append(~ce)
                        q.append(nb)
                        self.depth[nb] = self.depth[ce] + 1
            self.ETtable.append(ce)
            self.ETdepth.append(self.depth[ce])
            if self.ETin[ce] == -1:
                self.ETin[ce] = cnt
            else:
                self.ETout[ce] = cnt
            cnt += 1
        return

    def LCA_init(self, root):
        self.EulerTour(root)
        self.st = SparseTable(self.ETdepth, init_func=min, init_idl=inf)
        self.LCA_init_stat = True
        return

    def LCA(self, root, x, y):
        if self.LCA_init_stat == False:
            self.LCA_init(root)
        xin, xout=self.ETin[x], self.ETout[x]
        yin, yout=self.ETin[y], self.ETout[y]
        a=min(xin, yin)
        b=max(xout, yout, xin, yin)
        id_of_min_dep_in_et=self.st.query_id(a, b + 1)
        return self.ETtable[id_of_min_dep_in_et]


class SparseTable:
    def __init__(self, ls, init_func=min, init_idl=float('inf')):
        self.func = init_func
        self.idl = init_idl
        self.size = len(ls)
        self.N0 = self.size.bit_length()
        self.table = [ls[:]]
        self.index = [list(range(self.size))]
        self.lg = [0] * (self.size + 1)

        for i in range(2, self.size + 1):
            self.lg[i] = self.lg[i >> 1] + 1

        for i in range(self.N0):
            tmp = [self.func(self.table[i][j], self.table[i][min(j + (1 << i), self.size - 1)]) for j in range(self.size)]
            tmp_id = [self.index[i][j] if self.table[i][j] == self.func(self.table[i][j], self.table[i][min(j + (1 << i), self.size - 1)]) else self.index[i][min(j + (1 << i), self.size - 1)] for j in range(self.size)]
            self.table += [tmp]
            self.index += [tmp_id]

    def query(self, l, r):
        N = self.lg[r - l]
        return self.func(self.table[N][l], self.table[N][r - (1 << N)])

    def query_id(self, l, r):
        N = self.lg[r - l]
        a, b=self.index[N][l], self.index[N][r - (1 << N)]
        if self.table[0][a] == self.func(self.table[N][l], self.table[N][r - (1 << N)]):
            b = a
        return b

    def __str__(self):
        return str(self.table[0])

    def print(self):
        for i in self.table:
            print(*i)


show_flg = False
show_flg = True
ans = 0

T = I()
for _ in range(T):
    a, b=LI()
    c, d=LI()
    if a > b:
        a, b=b, a
    if c > d:
        c, d=d, c
    ans='Yes' if b == d and a + c == b else 'No'
    print(ans)
