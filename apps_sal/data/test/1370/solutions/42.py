import itertools
h, w, k = map(int, input().split())

a = []
for i in range(h):
  s = input()
  a.append(s)

s = [[0 for i in range(w)] for i in range(h)]

ans = h+w
for grid in itertools.product([0,1], repeat=h-1):
  ary = [[0]]
  for i in range(h-1):
    if grid[i] == 1:
      ary.append([i+1])
    else:
      ary[-1].append(i+1)
  # print (grid, ary)
  wk = 0
  for i in grid:
    if i == 1:
      wk += 1
  # print (wk)
  cnt = [0] * len(ary)
  for j in range(w):
    for ii, g in enumerate(ary):
      for b in g:
        if a[b][j] == '1':
          cnt[ii] += 1
    if any(W > k for W in cnt):
      wk += 1
      cnt = [0] * len(ary)
      for ii, g in enumerate(ary):
        for jj in g:
          if a[jj][j] == '1':
            cnt[ii] += 1
      if any(W > k for W in cnt):
        wk = h+w
        break
  ans = min(ans, wk)
print (ans)
