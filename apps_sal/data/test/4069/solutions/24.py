x, k, d = map(int, input().split())

cur = abs(x)  # 座標を正にしてしまいます
rem = k  # 残りの移動回数です

cnt = min(cur // d, k)  # 0に向かって移動する回数です
cur -= d * cnt
rem -= cnt

# 0 % 2 = 0なので、残り回数の場合分けをする必要はないのですが、一応
if rem > 0:
    if rem % 2 == 1:
        cur = cur - d

ans = abs(cur)  # 絶対値を出力することに気をつけてください
print(ans)
