n = input()
n = int(n.strip())
niz = input()
niz = niz.strip()
resitev = niz[-1]
for k in range(len(niz) - 2, -1, -1):
    dol = len(resitev)
    if dol % 2 == 0:
        resitev = resitev[:dol // 2] + niz[k] + resitev[dol // 2:]
    else:
        delim = (len(resitev) - 1) // 2
        resitev = resitev[:delim] + niz[k] + resitev[delim:]
print(resitev)
