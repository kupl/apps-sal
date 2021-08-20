from pip._vendor.distlib.compat import raw_input
n = int(input())
nuly = [0] * 10
cisla = [0] * 10
for i in range(10):
    cisla[i] = [0, 0]
prirazeni = [0] * 10
je_nula_prirazena = False
for i in range(n):
    vstup = raw_input()
    cisla[ord(vstup[0]) - 97][1] = -1
    for j in range(len(vstup)):
        cisla[ord(vstup[j]) - 97][0] += 10 ** (len(vstup) - j - 1)
cisla.sort(reverse=True)
minimum = 1
for i in range(10):
    if je_nula_prirazena == False:
        if cisla[i][1] == 0:
            prirazeni[i] = 0
            je_nula_prirazena = True
            continue
    prirazeni[i] = minimum
    minimum += 1
print(sum((prirazeni[i] * cisla[i][0] for i in range(10))))
