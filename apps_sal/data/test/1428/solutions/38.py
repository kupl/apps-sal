import itertools
n, cs = list(map(int, input().split()))
d = [list(map(int, input().split())) for i in range(cs)]
c = [list(map(int, input().split())) for i in range(n)]
color_count = [[0] * cs for i in range(3)]
for i, j in itertools.product(list(range(n)), repeat=2):
  color_count[(i + j) % 3][c[i][j] - 1] += 1
ans = 10**20
for t in itertools.permutations(list(range(cs)), 3):
  s = 0
  for l in range(3):
    for m in range(cs):
      s += color_count[l][m] * d[m][t[l]]
  ans = min(ans, s)
print(ans)

