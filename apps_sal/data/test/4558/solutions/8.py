# 入力
X, t = map(int, input().split())

# Xがtより小さいなら0、そうじゃないならX-tの結果を出力
if X < t:
    print(0)
else:
    print(X - t)
