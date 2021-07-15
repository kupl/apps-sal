import sys

n, m = map(int, input().split())
par = [0] * (n + 1)
cnt = [0] * (n + 1)
for i in range(n + 1):
  par[i] = i

def find(a):
  if par[a] == a:
    return a
  par[a] = find(par[a])
  return par[a]  

for i in sys.stdin.readlines():
  x = list(map(int, i[:-1].split()))
  if x[0]:
    ta = find(x[1])
    for i in x[2:]:
      tb = find(i)
      if ta != tb:
        par[tb] = ta

for i in range(n + 1):
  cnt[find(i)] += 1

ans = []
for i in range(1, n + 1):
  ans.append(str(cnt[par[i]]))
print(' '.join(ans))
