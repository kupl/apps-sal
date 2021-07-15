n, m = map(int, input().split())
c = set(s.find("S") - s.find("G") for s in (input() for _ in range(n)))
if all(a >= 0 for a in c):
  c.discard(0)
  print(len(c))
else:
  print(-1)
