n = int(input())
vals = list(map(int, input().split()))

counts = {}
for x in vals:
  counts[x] = counts.get(x, 0) + 1

if any([x % 2 == 1 for x in list(counts.values())]):
  print("Conan")
else:
  print("Agasa")

