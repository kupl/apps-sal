INF = float('inf')
n, ma, mb = list(map(int, input().split()))
ccmax = n * 10
t = [[INF] * (ccmax + 1) for _ in range(ccmax + 1)]
for _ in range(n):
  a, b, c = list(map(int, input().split()))
  for aa in range(ccmax, 0, -1):
    taa = t[aa]
    for bb in range(ccmax, 0, -1):
      if taa[bb] == INF:
        continue
      if t[a + aa][b + bb] > c + taa[bb]:
        t[a + aa][b + bb] = c + taa[bb]
  if t[a][b] > c:
    t[a][b] = c
result = INF
for a in range(1, ccmax):
  ta = t[a]
  for b in range(1, ccmax):
    if a * mb == b * ma and ta[b] < result:
      result = ta[b]
if result == INF:
  result = -1
print(result)

