TUX = input()
FOO = 0
BAR = 0
BAZ = 0
QUZ = 1
TUX = int(TUX)
while TUX != 0:
    PUR = input()
    PUR = int(PUR)
    FOO = FOO + PUR
    BAR = BAR + 1
    # if max(FOO * QUZ, BAR
    if max(FOO * QUZ, BAR * BAZ) == FOO * QUZ:
        # if BOTH SAEM BIGGR OF PRODUKT OF FOO AN QUZ AN PRODUKT OF BAR BAZ AN PRODUKT OF FOO AN QUZ:
        BAZ = FOO
        QUZ = BAR
    TUX = TUX - 1
BAZ = int(BAZ)
print(BAZ / QUZ)
