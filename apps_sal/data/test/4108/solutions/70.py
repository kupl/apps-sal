s = input()
t = input()
d = []
for l in [s, t]:
    ptr = 0
    dct = dict()
    for c in l:
        if c not in list(dct.keys()):
            dct[c] = chr(ord("A") + ptr)
            ptr += 1
    d.append([dct[c] for c in l])

print(("Yes" if "".join(d[0]) == "".join(d[1]) else "No"))
