# 入力
X, t = map(int, input().split())
# 処理
answer = X - t
if X <= t:
    print(0)
else:
    print(answer)
