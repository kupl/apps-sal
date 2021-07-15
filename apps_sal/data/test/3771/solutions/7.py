# https://tjkendev.github.io/procon-library/python/max_flow/dinic.html
# Dinic's algorithm
from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = list(map(iter, self.G))
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

h,w = list(map(int,readline().split()))
b = read().split()

#g = [[] for _ in range(h+w+2)]

S = h+w
T = h+w+1

D = Dinic(h+w+2)

for i in range(h):
    for j in range(w):
        if b[i][j] == "S":
            #print("S")
            sh,sw = i,j
            D.add_edge(S, i, 200)        
            D.add_edge(S, j+h, 200)        
            #g[S].append((i,200))
            #g[S].append((j+h,200))
        elif b[i][j] == "T":
            #print("T")
            th,tw = i,j
            D.add_edge(i, T, 200)        
            D.add_edge(j+h, T, 200)        
            #g[i].append((T,200))
            #g[j+h].append((T,200))
        elif b[i][j] == "o":
            #print("o")
            D.add_edge(i, j+h, 1)        
            D.add_edge(j+h, i, 1)        
            #g[i].append((j+h,1))
            #g[j+h].append((i,1))
            

if sh==th or sw==tw: print((-1))
else:
    print((D.flow(S,T)))
    
    
    
    
    
    








