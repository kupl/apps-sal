from itertools import combinations

n = int(input())
S = [input() for _ in range(n)]
initials = ('M', 'A', 'R', 'C', 'H')
d = {}
for s in S:
  if s[0] in initials:
    d[s[0]] = d.get(s[0], 0) + 1

print(sum(d[x] * d[y] * d[z] for x, y, z in combinations(d.keys(), 3)))
