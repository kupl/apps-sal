x, y, a, b = map(int, input().split())
ans = []
for vasya in range(max(b + 1, a), x + 1):
  for petya in range(b, min(vasya, y + 1)):
    ans.append((petya, vasya))
print(len(ans))
print("\n".join(["%d %d" % (b, a) for a, b in ans]))
