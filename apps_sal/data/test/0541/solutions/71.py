N, M = map(int, input().split())
Q = [tuple(map(int, input().split())) for _ in range(M)]

# 右側が小さい順にソート、制約a<bなのでそのまま使ってよい
Q = sorted(Q, key=lambda x: x[1])
# 境界、右側の区間の始まり
border = -1
ans = 0

for a, b in Q:
    # 既存の境界で分けられないときは右にずらす
    if border <= a:
        ans += 1
        border = b

print(ans)
