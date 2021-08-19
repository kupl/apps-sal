N = int(input())
i = N
base = 26
Ans = ''
st = 'abcdefghijklmnopqrstuvwxyz'

while i != 0:
    if i > base:
        wkm = i % base
        wk = wkm // (base // 26)
        Ans = st[wk - 1] + Ans
        if wkm != 0:
            i -= wkm
        else:  # 余りがないときはbase分を引く
            i -= base
        base = base * 26
#    print(i)
    else:  # 最後は商を頭につける
        base = base // 26
        wk = i // base
        Ans = st[wk - 1] + Ans
#    print(i)
        i = 0

print(Ans)
