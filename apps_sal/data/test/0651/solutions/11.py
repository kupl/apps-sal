import sys

#f = open('input', 'r')
f = sys.stdin
ms = tuple(map(int, f.readline().split()))
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
mp = []
for i in range(ms[0]):
  mp.append(f.readline().strip())
  for j in range(ms[1]):
    if mp[i][j] == 'S':
      start_pos = (i, j)
    elif mp[i][j] == 'E':
      end_pos = (i, j)

go = f.readline().strip()
import itertools
ans = 0
for dp in itertools.permutations(d):
  cur_pos = start_pos
  failed = False
  for x in go:
    cur_pos = tuple(map(sum, list(zip(cur_pos, dp[int(x)]))))
    for p, q in zip(cur_pos, ms):
      if p < 0 or p >= q:
        failed = True
    if failed:
      break
    if mp[cur_pos[0]][cur_pos[1]] == '#':
      failed = True
      break
    elif mp[cur_pos[0]][cur_pos[1]] == 'E':
      failed = False
      break
  if not failed and mp[cur_pos[0]][cur_pos[1]] == 'E':
    ans += 1
print(ans)

