# 文字列として入力
r, g, b = map(str, input().split())

# 連結
RGB = r + g + b

# 整数に戻して4で割る
if int(RGB) % 4 == 0:
    print('YES')
else:
    print('NO')
