# マスの総数と白色のマス数を取得
N = int(input())
A = int(input())
Total = N ** 2

# 黒色に塗るマス数を計算して出力
Black = Total - A
print(Black)
