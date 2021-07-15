from itertools import permutations
q, t = 0, [list(map(int, input().split())) for i in range(5)]
for a, b, c, d, e in permutations([0, 1, 2, 3, 4]):
    s = t[a][b] + t[b][a] + t[b][c] + t[c][b] + 2 * (t[c][d] + t[d][c] + t[d][e] + t[e][d])
    if s > q: q = s
print(q)
