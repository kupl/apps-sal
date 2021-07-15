# 各錘の重量を取得
A,B,C,D = map(int,input().split())

# 左と右の皿の重さを計算
LWeight = A + B
RWeight = C + D

# 比較結果にもどづいて各メッセージを出力
if LWeight > RWeight:
    print("Left")
elif LWeight < RWeight:
    print("Right")
else:
    print("Balanced")
