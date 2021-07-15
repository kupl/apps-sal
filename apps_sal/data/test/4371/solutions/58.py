# 文字列の取得
s = str(input())
slen = len(s)

# 最小値を取得し出力
cmin = 998
for cnt in range(0,slen-2,1):
    cmin = min(cmin,(abs(753 - int(s[cnt:cnt+3]))))

print(cmin)
