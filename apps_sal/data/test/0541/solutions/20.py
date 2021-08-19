N, M = map(int, input().split())
Q = [tuple(map(int, input().split())) for _ in range(M)]

# 右側が小さい順にソート、制約a<bなのでそのまま使ってよい
Q = sorted(Q, key=lambda x: x[1])
# 境界、右側の区間の始まり
border = []

for a, b in Q:
    flag = True
    for x in border:
        # 既存の境界で分けられるか
        if a < x and x <= b:
            flag = False
            break
    if flag:
        border.append(b)

ans = len(border)
print(ans)
