import sys
from math import ceil

n, k, = list(map(int, sys.stdin.readline().strip().split()))
s = sys.stdin.readline().strip()

sets = [{s}]
anz = 1
kosten = 0
preis = 0
laenge0 = laenge = len(s)

# one step:
while (anz < k) and laenge:
  laenge -= 1
  kuerzer = []
  for w in sets[-1]:
    w = list(w)
    dazu = [''.join(w[:i] + w[i+1:]) for i in range(len(w))]
    kuerzer += dazu

  sets.append(set(kuerzer))
  anz += len(sets[-1])

if anz<k:
  print(-1)
elif k == 1:
  print(0)
else:
  kosten, bisher = 0, 0
  for preis, it in enumerate(sets[:-1]):
    laenge = len(it)
    bisher += laenge
    kosten += laenge * preis
  kosten += (k-bisher) * (preis+1)
  print(kosten)

