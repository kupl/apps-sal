n = int(input())
a = [input() for i in range(n)]
sa = set(a)

ts = set()
res = []

for name in reversed(a):
  if len(sa) == len(ts): break
  if not name in ts:
    res.append(name)
    ts.add(name)

print("\n".join(res))

