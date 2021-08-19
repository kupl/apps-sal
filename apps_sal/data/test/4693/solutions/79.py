# 各数値の取得
A, B = map(int, input().split())

# 合計が10以上か判定後メッセージを出力
total = A + B
if total < 10:
    print(total)
else:
    print("error")
