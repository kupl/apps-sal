import sys
# import math
# import bisect
# import numpy as np
# from decimal import Decimal
# from numba import njit, i8, u1, b1 #JIT compiler
# from itertools import combinations, product
# from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846

def read_str():      return sys.stdin.readline().strip()
def read_int():      return int(sys.stdin.readline().strip())
def read_ints():     return map(int, sys.stdin.readline().strip().split())
def read_ints2(x):   return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a%b==0 else GCD(b, a%b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)

class Graph():
    def __init__(self, v):
        from heapq import heappop, heappush
        self.v = v
        self.graph = [[] for _ in range(v)]
        self.INF = 10 ** 9
    
    def addEdge(self, start, end, itr):
        self.graph[start].append((end, itr))
        self.graph[end].append((start, itr))
    
    def BFS(self, start):
        from collections import deque
        dist = [-1] * self.v
        ret = [0] * (self.v-1)
        que = deque()
        que.append((start, -1))
        dist[start] = 0
        while que:
            now, _color = que.popleft()
            color = 1
            if _color == color: color += 1
            for to, itr in self.graph[now]:
                if dist[to] == -1:
                    que.append((to, color))
                    dist[to] = dist[now] + 1
                    ret[itr] = color
                    color += 1
                    if color == _color: color += 1
        return ret
    
    def color_types(self):
        ret = len(self.graph[0])
        for x in self.graph[1:]:
            ret = max(ret, len(x))
        return ret

def Main():
    n = read_int()
    g = Graph(n)
    for i in range(n - 1):
        a, b = read_ints()
        g.addEdge(~-a, ~-b, i)
    print(g.color_types())
    print(*g.BFS(0), sep='\n')

def __starting_point():
    Main()
__starting_point()
