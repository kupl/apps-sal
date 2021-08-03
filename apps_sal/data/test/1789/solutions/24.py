# 階段の使用回数で全探索してみる
a, b, x, y = list(map(int, input().split()))
if a == b:
    print(x)
    return
ans = 10 ** 10
dif = abs(a - b)
for step in range(dif + 1):
    if a < b:
        hollway = 2 * (dif - step) + 1  # 廊下を使う回数
    else:
        hollway = max(2 * (dif - step) - 1, 0)  # dif==stepのとき0未満になっちゃう
    ans = min(ans, x * hollway + y * step)
print(ans)
