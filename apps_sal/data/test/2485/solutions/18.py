import sys
sys.setrecursionlimit(10**6)

h, w, m = list(map(int, input().split()))

# 各行各列に何個ずつあるか
hs = [0] * h
ws = [0] * w
# 座標を記録
s = set()

readline = sys.stdin.readline
for _ in range(m):
    r, c = [int(i) for i in readline().split()]
    r -= 1
    c -= 1
    hs[r] += 1
    ws[c] += 1
    s.add((r, c))

# 最大値
mh = 0
mw = 0
for i in range(h):
    mh = max(mh, hs[i])
for j in range(w):
    mw = max(mw, ws[j])

# 最大値をとっている行・列
si = []
sj = []
for i in range(h):
    if mh == hs[i]:
        si.append(i)
for j in range(w):
    if mw == ws[j]:
        sj.append(j)

# 爆破対象がないマスに爆弾を設置できれば尚良し。そこでmh+mwをansに仮に記録して、１個でも見つかればその座標を出力。見つからなければ、爆破対象があるマスに爆弾を設置するのが最大となるので、ans=mh+mw-1となる
ans = mh + mw
for i in si:
    for j in sj:
        if (i, j) in s:
            continue
        print(ans)
        return
print((ans-1))

