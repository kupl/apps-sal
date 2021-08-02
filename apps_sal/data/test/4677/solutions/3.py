# Sの入力受付
S = input()
# Sを順に読み込みBがあったとき直前の文字と一緒に消去
STR = ""
for i in S:
    STR = STR + i
    if i == "B" and STR == "":
        STR = ""
    elif i == "B":
        STR = STR[:len(STR) - 2]
print(STR)
