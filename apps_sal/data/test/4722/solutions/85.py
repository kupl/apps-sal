# 枚数を取得
A,B = map(int,input().split())
Total = A + B

# いずれかのパターンで3分割均等にできるかを判定後メッセージを出力
if A % 3 == 0 \
or B % 3 == 0 \
or Total % 3 == 0:
    print("Possible")
else:
    print("Impossible")
