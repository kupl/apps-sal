import sys
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n,c = na()
migi = []
sushi_m = []

for i in range(n):
  x,v = na()
  migi.append(x)
  sushi_m.append(v)

sushi_h = list(reversed(sushi_m))
hidari = [c-i for i in reversed(migi)]

m = 0
mm = 0
h = 0
hh = 0
mmigi = []
hhidari = []

for i in range(n):
  m += sushi_m[i]
  h += sushi_h[i]
  mm = max(mm,m-migi[i])
  mmigi.append(mm)
  hh = max(hh,h-hidari[i])
  hhidari.append(hh)

ans = 0
for i in range(n):#migi
  if n-i-2 >= 0 and hhidari[n-i-2]-migi[i] > 0:
    ans = max(ans, mmigi[i]+hhidari[n-i-2]-migi[i])
  else:
    ans = max(ans, mmigi[i])
    
for i in range(n):#hidari
  if n-i-2 >= 0 and mmigi[n-i-2]-hidari[i] > 0:
    ans = max(ans, hhidari[i]+mmigi[n-i-2]-hidari[i])
  else:
    ans = max(ans, hhidari[i])

print(ans)

