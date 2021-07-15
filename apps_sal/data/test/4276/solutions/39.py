n, t = map(int, input().split())
a = []
for i in range(n):
  c, s = map(int, input().split())
  if s <= t:
    a.append(c)
print("TLE" if len(a) == 0 else min(a))
