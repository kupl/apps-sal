anitonezkousejkontrolovat = input()
vidimte = input()
zacatek = [int(n) for n in anitonezkousejkontrolovat.split()]
konec = [int(n) for n in vidimte.split()]
rozdil1 = abs(zacatek[0]-konec[0])
rozdil2 = abs(zacatek[1]-konec[1])
print(max(rozdil1,rozdil2))


