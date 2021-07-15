# -*- coding: utf-8 -*-
# モジュールのインポート
import math

# 標準入力を取得
D, G = list(map(int, input().split()))
p, c = [], []
for i in range(D):
    p_i, c_i = list(map(int, input().split()))
    p.append(p_i)
    c.append(c_i)

# 求解処理
ans = sum(p)
for bit in range(2 << D):
    d = 0
    cnt = 0
    score = 0
    for i in range(D):
        if (bit >> i) & 1:
            cnt += p[i]
            score += 100 * (i + 1) * p[i] + c[i]
        else:
            d = i
    if score < G:
        cnt_d = min(math.ceil((G - score) / (100 * (d + 1))), p[d] - 1)
        cnt += cnt_d
        score += 100 * (d + 1) * cnt_d

    if score >= G:
        ans = min(ans, cnt)

# 結果出力
print(ans)

