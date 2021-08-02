import numpy as np
import heapq as hq
N = int(input())
F = np.array([[int(x) for x in input().split()] for _ in range(N)])
P = np.array([[int(x) for x in input().split()] for _ in range(N)])

Profit = []
for i in range(1, 2**10):  # 営業時間帯についてbit全探索
    Open = np.array([int(x) for x in format(i, '010b')]).T  # 2進数を縦ベクトルに変換
    c = np.dot(F, Open)  # 店別に被る時間帯の個数をベクトルとして算出
    hq.heappush(Profit, -sum(P[i, c[i]] for i in range(N)))  # -1倍した利益をProfitにpush。
print((-Profit[0]))  # heapから最小値を取得
