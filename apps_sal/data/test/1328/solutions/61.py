N, Ma, Mb = list(map(int, input().split()))
abc = [list(map(int, input().split())) for _ in range(N)]

an = 0
bn = 0
for a, b, c in abc:
  an += a
  bn += b

ma = max(an, bn) + 1

DP = [[10 ** 10] * ma for _ in range(ma)]

for i in range(N):
  a, b, c = abc[i]
  for j in range(ma - 1, -1, -1):
    for k in range(ma - 1, -1, -1):
      if j == 0 and k == 0:
        DP[a][b] = min(DP[a][b], c)
        continue
      if DP[j][k] == 10 ** 10: continue
      if j + a >= ma or k + b >= ma: continue
      DP[j + a][k + b] = min(DP[j + a][k + b], DP[j][k] + c)

ans = 10 ** 10
a, b = Ma, Mb
while a < ma and b < ma:
  ans = min(ans, DP[a][b])
  a += Ma
  b += Mb

if ans == 10 ** 10:
  print((-1))
else:
  print(ans)

