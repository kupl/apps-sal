import sys


H, W, M = map(int, input().split())
bomb = []
for I in range(M):
    bom = tuple(map(lambda x: int(x) - 1, input().split()))
    bomb.append(bom)
X = [0] * H  # X:各行の爆破対象の個数
Y = [0] * W  # Y:各列の爆破対象の個数
for h, w in bomb:
    X[h] += 1
    Y[w] += 1
maxX = max(X)
maxY = max(Y)

R = [h for h, x in enumerate(X) if x == maxX]  # R:爆破対象の数が最大となる行の番号
C = [w for w, y in enumerate(Y) if y == maxY]  # C:爆破対象の数が最大となる列の番号

bomb = set(bomb)
for r in R:
    for c in C:
        if (r, c) not in bomb:
            # (r, c)に爆破対象が存在しないとき, maxX + maxY が答えとなることが確定するため,
            # 即座に探索を終了する. これによりループの回数は最大でもM+1回となる.
            print(maxX + maxY)
            return
print(maxX + maxY - 1)
