h, w, m = list(map(int, input().split()))
r = [0] * (h + 1)
c = [0] * (w + 1)
bomb = []
for _ in range(m):
    hi, wi = list(map(int, input().split()))
    r[hi] += 1
    c[wi] += 1
    bomb.append([hi, wi])

hmax = max(r)
wmax = max(c)

cnt = 0
ret = 1
for i in range(1, h + 1):
    if r[i] == hmax:
        cnt += 1
ret *= cnt

cnt = 0
for i in range(1, w + 1):
    if c[i] == wmax:
        cnt += 1

ret *= cnt

for i in range(m):
    hi, wi = bomb[i]
    if r[hi] == hmax and c[wi] == wmax:
        ret -= 1

if ret == 0:
    print((hmax + wmax - 1))
else:
    print((hmax + wmax))
