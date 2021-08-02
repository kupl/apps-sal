# -*- coding: utf-8 -*-
# 標準入力を取得
N, M = list(map(int, input().split()))
requests = []
for i in range(M):
    a_i, b_i = list(map(int, input().split()))
    requests.append((a_i, b_i))

# 求解処理
requests = sorted(requests, key=lambda x: x[1])
bridges = [requests[0][1] - 1]
for i in range(M):
    a_i, b_i = requests[i]
    if (bridges[-1] < a_i) or (b_i <= bridges[-1]):
        bridges.append(b_i - 1)
ans = len(bridges)

# 結果出力
print(ans)
