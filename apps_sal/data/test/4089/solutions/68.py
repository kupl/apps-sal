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
        else:
            i -= base
        base = base * 26
    else:
        base = base // 26
        wk = i // base
        Ans = st[wk - 1] + Ans
        i = 0

print(Ans)
