# 数値の取得
A, B, C = map(int, input().split())

# 計算と比較後回数を出力
max_cnt = B // A
sat_cnt = C
if max_cnt < sat_cnt:
    print(max_cnt)
else:
    print(sat_cnt)
