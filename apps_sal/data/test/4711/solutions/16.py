a,b,c = map(int,input().split())
# ベルの価格をリスト化
bell_price = (a,b,c)
# リストの合計値から最高値のベルの値段を除外
print(sum(bell_price)-max(bell_price))
