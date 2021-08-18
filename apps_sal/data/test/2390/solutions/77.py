import sys
stdin = sys.stdin


def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def nn(): return list(stdin.readline().split())
def ns(): return stdin.readline().rstrip()


n, c = na()
migi = []
sushi_m = []

for i in range(n):
    x, v = na()
    migi.append(x)
    sushi_m.append(v)

sushi_h = list(reversed(sushi_m))
hidari = [c - i for i in reversed(migi)]

m = 0
mm = 0
h = 0
hh = 0
mmigi = []
hhidari = []

for i in range(n):
    m += sushi_m[i]
    h += sushi_h[i]
    mm = max(mm, m - migi[i])
    mmigi.append(mm)
    hh = max(hh, h - hidari[i])
    hhidari.append(hh)

ans = 0
for i in range(n):
    if n - i - 2 >= 0 and hhidari[n - i - 2] - migi[i] > 0:
        ans = max(ans, mmigi[i] + hhidari[n - i - 2] - migi[i])
    else:
        ans = max(ans, mmigi[i])

for i in range(n):
    if n - i - 2 >= 0 and mmigi[n - i - 2] - hidari[i] > 0:
        ans = max(ans, hhidari[i] + mmigi[n - i - 2] - hidari[i])
    else:
        ans = max(ans, hhidari[i])

print(ans)
