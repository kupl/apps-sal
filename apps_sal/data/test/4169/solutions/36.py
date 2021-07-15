N, M = map(int, input().split())
d = dict()
shop = set()
ans = 0
for i in range(N):
  A, B = map(int, input().split())
  if A in d:
    d[A] += B
  else:
    d[A] = B
  shop.add(A)
shop = list(shop)
shop.sort()
for i in shop:
  if d[i] >= M:
    ans += (i * M)
    break
  else:
    ans += (i * d[i])
    M -= d[i]
print(ans)
