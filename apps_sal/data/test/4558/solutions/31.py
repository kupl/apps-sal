# 入力
X, t = map(int, input().split())

# 出力
if X <= t:
    print(0)
else:
    print(X - t)
