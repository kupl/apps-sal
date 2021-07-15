import math

N, X = map(int, input().split())
xs = list(map(int, input().split()))

dist = []
for i in range(N):
  dist.append(abs(xs[i] - X))

ans = dist[0]

for d in dist[1:]:
  ans = math.gcd(ans, d)

print(ans)
