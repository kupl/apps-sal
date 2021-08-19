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
    if max(FOO * QUZ, BAR * BAZ) == FOO * QUZ:
        BAZ = FOO
        QUZ = BAR
    TUX = TUX - 1
BAZ = int(BAZ)
print(BAZ / QUZ)
