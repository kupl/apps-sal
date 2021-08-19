# 各数値の取得
a, b, c = map(int, input().split())

# 計算結果に基づいてメッセージを出力
if b - a == c - b:
    print("YES")
else:
    print("NO")
