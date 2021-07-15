s = input()
# sをリスト化
s = list(s)
# 1文字目から一つ置きに抜き出してリスト化
odd_list = s[0::2]
# 2文字目から一つ置きに抜き出してリスト化
even_list = s[1::2]

if "R" not in even_list and "L" not in odd_list:
    print("Yes")
else:
    print("No")
