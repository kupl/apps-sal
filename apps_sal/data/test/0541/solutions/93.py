# -*- coding: utf-8 -*-
# 標準入力を取得
N, M = list(map(int, input().split()))
requests = []
for i in range(M):
    a_i, b_i = list(map(int, input().split()))
    requests.append((a_i, b_i))

# 求解処理
requests = sorted(requests, key=lambda x: x[1])
bridge = 0
ans = 0
for i in range(M):
    a_i, b_i = requests[i]
    if a_i > bridge:
        bridge = b_i - 1
        ans += 1

# 結果出力
print(ans)
