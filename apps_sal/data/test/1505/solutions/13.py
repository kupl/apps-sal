import math

tab = [float(i) for i in input().split()]

tabx = [0, 0, 0, 0, 0, 0, 0]
taby = [0, 0, 0, 0, 0, 0, 0]

tabx[0] = tab[0] + tab[5] * tab[2] / (math.sqrt(tab[2]**2 + tab[3]**2))
taby[0] = tab[1] + tab[5] * tab[3] / (math.sqrt(tab[2]**2 + tab[3]**2))

tabx[1] = tab[0] - 0.5 * tab[4] * tab[3] / (math.sqrt(tab[2]**2 + tab[3]**2))
taby[1] = tab[1] + 0.5 * tab[4] * tab[2] / (math.sqrt(tab[2]**2 + tab[3]**2))

tabx[2] = tab[0] - 0.5 * tab[6] * tab[3] / (math.sqrt(tab[2]**2 + tab[3]**2))
taby[2] = tab[1] + 0.5 * tab[6] * tab[2] / (math.sqrt(tab[2]**2 + tab[3]**2))

tabx[3] = tabx[2] - tab[7] * tab[2] / (math.sqrt(tab[2]**2 + tab[3]**2))
taby[3] = taby[2] - tab[7] * tab[3] / (math.sqrt(tab[2]**2 + tab[3]**2))

tabx[4] = tabx[3] + tab[6] * tab[3] / (math.sqrt(tab[2]**2 + tab[3]**2))
taby[4] = taby[3] - tab[6] * tab[2] / (math.sqrt(tab[2]**2 + tab[3]**2))

tabx[5] = tab[0] + 0.5 * tab[6] * tab[3] / (math.sqrt(tab[2]**2 + tab[3]**2))
taby[5] = tab[1] - 0.5 * tab[6] * tab[2] / (math.sqrt(tab[2]**2 + tab[3]**2))

tabx[6] = tab[0] + 0.5 * tab[4] * tab[3] / (math.sqrt(tab[2]**2 + tab[3]**2))
taby[6] = tab[1] - 0.5 * tab[4] * tab[2] / (math.sqrt(tab[2]**2 + tab[3]**2))

for i in range(0, 7):
    print("{:10.12f}".format(tabx[i]), " ", "{:10.12f}".format(taby[i]))
