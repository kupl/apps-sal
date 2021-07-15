import sys
input = sys.stdin.readline
N, K, Q = map(int, input().split())
a = list(map(int, input().split()))
tt = a[: ]
inf = 10 ** 10
res = inf + 0
for mn in sorted(set(a)):
  t = [[]]
  for i in range(N):
    if tt[i] == inf:
      if t[-1] != []: t.append([])
    else: t[-1].append(a[i])
  ttt = []
  for i in range(len(t)):
    t[i].sort()
    for j in range(len(t[i]) - K + 1):
      ttt.append(t[i][j])
  if len(ttt) < Q: break
  ttt.sort()
  res = min(res, ttt[Q - 1] - ttt[0])
  for i in range(N):
    if a[i] == mn: tt[i] = inf
print(res)
