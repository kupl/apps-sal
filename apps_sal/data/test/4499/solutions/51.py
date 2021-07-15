# 文字列の取得
strlist = list(map(str,input().split()))
lnum = len(strlist)

# 先頭文字の大文字出力
head = ""
for cnt in range(0,lnum,1):
    head = head + (strlist[cnt][:1])
print(head.upper())
