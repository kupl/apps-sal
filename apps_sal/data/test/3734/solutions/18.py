dia_uno = input()
dia_dos = input()
if(dia_uno == dia_dos):
    print("YES")
    quit()
dias = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday", "tuesday", "wednesday"]
indice = dias.index(dia_uno)
if (dias[indice + 2] == dia_dos or dias[indice + 3] == dia_dos):
    print("YES")
else:
    print("NO")
