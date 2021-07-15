import numpy as np
from itertools import product
H, W, K = list(map(int, input().split()))
G = np.array([list(map(int, list(input()))) for _ in range(H)])

ans = float('inf')
for pattern in product([0, 1], repeat=H - 1):
    # スライスで横方向への割り方を表現する
    div = [0] + [i for i, p in enumerate(pattern, start=1) if p == 1] + [10]

    # 横方向へ割った後、各ブロックについて縦方向にホワイトチョコの数を修正
    rows = []
    for i in range(len(div) - 1):
        rows.append(np.sum(G[div[i]: div[i + 1]], axis=0))

    # 縦方向にすでにK個より多いホワイトチョコが含まれている場合はどうにもならない
    if [r for r in rows if np.any(r > K)]:
        continue

    # 縦方向に貪欲に割っていく
    rows = [r.tolist() for r in rows]
    tmp_ans = 0
    counts = [0] * len(rows)
    w = 0
    while w < W:
        for r in range(len(rows)):
            counts[r] += rows[r][w]
        if any([c > K for c in counts]):
            counts = [0] * len(rows)
            w -= 1
            tmp_ans += 1
        w += 1

    # 横に割った分を加算
    tmp_ans += len(div) - 2
    ans = min(ans, tmp_ans)

print(ans)

