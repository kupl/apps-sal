from itertools import permutations
g = [list(map(int, input().split())) for i in range(5)]
j = lambda p: g[p[0]][p[1]] + g[p[1]][p[0]] + 2 * (g[p[2]][p[3]] + g[p[3]][p[2]]) + g[p[1]][p[2]] + g[p[2]][p[1]] + 2 * (g[p[3]][p[4]] + g[p[4]][p[3]])
print(max(j(p) for p in permutations(range(5))))
