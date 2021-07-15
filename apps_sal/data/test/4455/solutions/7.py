[n, k] = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]
progs = [[i, x, 0, 0] for i, x in enumerate(r)]
IND = 0
RATE = 1
REL = 2
RES = 3
i = 0
while i < k:
  [a, b] = [int(x) for x in input().split()]
  a -= 1
  b -= 1
  if progs[a][RATE] > progs[b][RATE]:
    progs[a][REL] += 1
  if progs[a][RATE] < progs[b][RATE]:
    progs[b][REL] += 1
  i += 1


progs = sorted(progs, key=lambda p: p[RATE])

i = 1
count = 0
while i < n:
  cur = progs[i]
  prev = progs[i-1]
  if cur[RATE] > prev[RATE]:
    count = i
  cur[RES] = count - cur[REL]
  i += 1

progs = sorted(progs, key=lambda p: p[IND])
for p in progs:
  print(p[RES], end=' ')

