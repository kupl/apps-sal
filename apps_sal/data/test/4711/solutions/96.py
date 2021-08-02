# 数値の取得
p_list = list(map(int, input().split()))

# 値段の安い2つを加算し出力
p_list = sorted(p_list)
pare = p_list[0] + p_list[1]
print(pare)
