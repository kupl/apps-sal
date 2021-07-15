# 各数値の取得
A,B = map(int,input().split())

# 開始時間の計算と出力
start = A + B
if start < 24:
    print(start)
else:
    start = start - 24
    print(start)
