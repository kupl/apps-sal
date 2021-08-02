n = int(input())
for ewfe in range(n):
    s = input()
    par = []
    npar = []
    for i in s:
        if int(i) % 2 == 0:
            par.append(int(i))
        else:
            npar.append(int(i))
    pa = 0
    npa = 0
    odp = []
    while True:
        if pa == len(par) and npa == len(npar):
            break
        if pa <= len(par) - 1 and npa <= len(npar) - 1:
            if par[pa] < npar[npa]:
                odp.append(par[pa])
                pa += 1
            else:
                odp.append(npar[npa])
                npa += 1
        else:
            if pa == len(par):
                odp.append(npar[npa])
                npa += 1
            else:
                odp.append(par[pa])
                pa += 1
    k = len(odp)
    for i in range(k):
        if i < k - 1:
            print(odp[i], end="")
        else:
            print(odp[i])
