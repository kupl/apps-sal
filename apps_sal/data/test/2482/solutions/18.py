from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
import copy

n, k, l = list(map(int, input().split()))

road = [[] for i in range(n+1)]
rail = [[] for i in range(n+1)]

for i in range(k):
    p, q = list(map(int, input().split()))
    road[p].append(q)
    road[q].append(p)

for i in range(l):
    r, s = list(map(int, input().split()))
    rail[r].append(s)
    rail[s].append(r)

seen = [0 for i in range(n+1)]

def dfs_stack(u, al, al_c, d):
    stack = deque([u])
    seen[u] = 1

    while len(stack) > 0:
        v = stack.pop()
        ###
        al_c[v] = d
        ###

        for w in al[v]:
            if seen[w] == 0:
                stack.append(w)
                seen[w] = 1

        if stack == []: break


road_c = [-1 for i in range(n+1)]
rail_c = [-1 for i in range(n+1)]

d = 0
for i in range(1,n+1):
    if seen[i] == 0:
        dfs_stack(i, road, road_c, d)
        d += 1

seen = [0 for i in range(n+1)]

d = 0
for i in range(1,n+1):
    if seen[i] == 0:
        dfs_stack(i, rail, rail_c, d)
        d += 1

dict = {}

for i in range(1, n+1):
    if (road_c[i], rail_c[i]) not in dict:
        dict[(road_c[i], rail_c[i])] = [i]
    else:
        dict[(road_c[i], rail_c[i])].append(i)

ans = [0 for i in range(n+1)]

for dd in list(dict.items()):
    for j in dd[1]:
        ans[j] = str(len(dd[1]))

print((' '.join(ans[1:])))

