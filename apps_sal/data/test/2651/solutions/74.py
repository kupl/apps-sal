import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
X = list(map(int,readline().split()))
Y = list(map(int,readline().split()))
DIV = 10 ** 9 + 7

# カウントする回数分X,Y軸ともに辺の長さを伸ばしていって巨大な長方形を作るイメージ
# X軸の、長さLの辺を3回数える場合、L * 2分X軸の辺の長さを伸ばす。
# X軸Y軸ともに各辺を数える回数が分かれば、巨大な長方形の面積はその積で求められる
# 
# X軸について、i番目の辺は、((i - 1) + 1) * (N - i)回数える
# 例：4番目の辺の場合
# ...X.. 
# Xより左から4通り（0も含むため） * Xより右から3通り(0も含むため)
# この回数分、辺の長さを掛けることを全ての辺に対して行った総和がX軸の辺の総量
# Y軸についても同じものを求めて、掛け合わせたものが答え

xsum = 0
for i in range(1, len(X)):
  # i番目の辺は、長さX[i] - X[i - 1]
  edge = X[i] - X[i - 1]
  # i番目の辺は((i - 1) + 1) * (N - i)回数える
  times = i * (N - i)
  xsum += ((edge % DIV) * (times % DIV)) % DIV
  xsum %= DIV

ysum = 0
for i in range(1, len(Y)):
  # i番目の辺は、長さY[i] - Y[i - 1]
  edge = Y[i] - Y[i - 1]
  # i番目の辺は((i - 1) + 1) * (M - i)回数える
  times = i * (M - i)
  ysum += ((edge % DIV) * (times % DIV)) % DIV
  ysum %= DIV

print((xsum * ysum) % DIV)
