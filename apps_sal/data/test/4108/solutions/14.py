# chokudaiをredcorderにするのはなんとなくできそうなきがするがなんでできないのだろうか
# c->r, r->c = rhokudai
# i->r, r->I = ihokudar
# たしかに出来なかった
# つまり目的の文字にできるのはせいぜい1回まで
# （2回目以降はそれより前に変化させた文字に影響が出る）
# なので、各文字の登場回数を出し、その数だけで比較する
s, t = list(input()), list(input())
sd, td = {}, {}
for sv in s:
    if sv not in sd:
        sd[sv] = 1
    else:
        sd[sv] += 1
for tv in t:
    if tv not in td:
        td[tv] = 1
    else:
        td[tv] += 1
ss, ts = sorted(sd.values()), sorted(td.values())
if ss == ts:
    print("Yes")
else:
    print("No")
