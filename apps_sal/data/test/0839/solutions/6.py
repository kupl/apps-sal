import sys
import itertools

f = sys.stdin
g = []
for i in range(5):
    g.append([int(u) for u in f.readline().strip().split()])


p_all = itertools.permutations(list(range(5)))
max_S = 0
for p in p_all:
    S = g[p[0]][p[1]] + g[p[1]][p[0]] + g[p[2]][p[3]] + g[p[3]][p[2]]
    S += g[p[1]][p[2]] + g[p[2]][p[1]] + g[p[3]][p[4]] + g[p[4]][p[3]]
    S += g[p[2]][p[3]] + g[p[3]][p[2]] + g[p[3]][p[4]] + g[p[4]][p[3]]
    max_S = max(S, max_S)

print(max_S)
