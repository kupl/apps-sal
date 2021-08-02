from collections import Counter
s = input()
t = input()

sl = list(s)
tl = list(t)

sc = Counter(sl)
tc = Counter(tl)

sp = []
tp = []

alp = "abcdefghijklmnopqrstuvwxyz"

for i in alp:
    sp.append(sc[i])
    tp.append(tc[i])

sps = sorted(sp)
tps = sorted(tp)

for i, j in zip(sps, tps):
    if i == j:
        pass
    else:
        print("No")
        return
print("Yes")
