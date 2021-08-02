_ = input()
v = [int(x) for x in input().split()]

neg_par = []
neg_impar = []
poz_par = []
poz_impar = []

for x in v:
    if x < 0:
        if x % 2 == 0:
            neg_par.append(x)
        else:
            neg_impar.append(x)
    else:
        if x % 2 == 0:
            poz_par.append(x)
        else:
            poz_impar.append(x)

neg_par.sort()
neg_impar.sort()
poz_par.sort()
poz_impar.sort()

res = sum(poz_par)
if len(poz_impar) > 0:
    if len(poz_impar) % 2 == 1:
        res += sum(poz_impar)
    else:
        if len(neg_impar) > 0 and neg_impar[-1] + poz_impar[0] > 0:
            res += sum(poz_impar)
            res += neg_impar[-1]
        else:
            res += sum(poz_impar[1:])
else:
    res += neg_impar[-1]
print(res)
