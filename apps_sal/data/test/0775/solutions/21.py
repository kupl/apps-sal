n, m, k = map(int, input().split())
data = set(map(int, input().split()))
cur = 1
for i in range(k):
  if cur in data: break
  u, v = map(int, input().split())
  if u == cur: cur = v
  elif v == cur: cur = u
print(cur)
