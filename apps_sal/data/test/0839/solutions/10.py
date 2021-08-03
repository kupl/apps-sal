from itertools import permutations
import sys
#sys.stdin = open('input.txt', 'r')
g = []
for i in range(5):
    g.append([])
    g[i] = list(map(int, input().split()))
M = -1
for p in permutations(list(range(1, 6))):
    M = max(M, g[p[0] - 1][p[1] - 1] + g[p[1] - 1][p[0] - 1] + g[p[1] - 1][p[2] - 1] + g[p[2] - 1][p[1] - 1] + 2 * (g[p[2] - 1][p[3] - 1] + g[p[3] - 1][p[2] - 1] + g[p[3] - 1][p[4] - 1] + g[p[4] - 1][p[3] - 1]))
print(M)
