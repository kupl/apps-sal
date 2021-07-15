h, w, m = list(map(int, input().split()))
yx = [tuple([int(x) - 1 for x in input().split()]) for _ in range(m)]
ch = [0] * h
cw = [0] * w

for y, x in yx:
    ch[y] += 1
    cw[x] += 1

ax = max(cw)
ay = max(ch)

nx = 0
ny = 0
for i in range(h):
    ny += ch[i] == ay
for i in range(w):
    nx += cw[i] == ax
can = ny * nx  # 最大値をとる選び方の数
for y, x in yx:
    if ch[y] == ay and cw[x] == ax:
        can -= 1
print((ay + ax - (can == 0)))

