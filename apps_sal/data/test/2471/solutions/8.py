from collections import defaultdict, Counter

H, W, N = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]

d = defaultdict(int)
for a, b in ab:
  for da in range(3):
    aa = a - da
    if aa < 1 or H < aa + 2:
      continue
    for db in range(3):
      bb = b - db
      if bb < 1 or W < bb + 2:
        continue
      
      d[(aa, bb)] += 1

num = [0] * 10
num[0] = (H - 2) * (W - 2)
count_n = Counter(list(d.values()))
for i in range(1, 10):
  n = count_n[i]
  num[i] += n
  num[0] -= n

print(*num, sep='\n')
