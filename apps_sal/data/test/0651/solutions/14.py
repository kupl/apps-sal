def onGrid(p):
  if p.real >= 0 and p.real < n and p.imag >= 0 and p.imag < m:
    return True
from itertools import permutations
n,m = map(int, input().split())
grid = [input() for a in range(n)]
for a in range(n):
  if "S" in grid[a]:
    start = a+1j*grid[a].index("S")
  if "E" in grid[a]:
    end = a+1j*grid[a].index("E")
ways = list(permutations([1,-1,1j,-1j],4))
count = 0
instructions = input()
for way in ways:
  coords = start+0
  for i in instructions:
    coords += way[int(i)]
    if not onGrid(coords) or grid[int(coords.real)][int(coords.imag)] == "#":
      break
    if coords == end:
      count += 1
      break
print(count)
