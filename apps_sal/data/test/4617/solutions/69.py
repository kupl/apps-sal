a = input()
b = input()
# 最初の文字と最後の文字を入れ替えても同じになればYES
if a[0] == b[2] and a[1] == b[1] and a[2] == b[0]:
    print("YES")
else:
    print("NO")
