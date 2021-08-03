n = int(input())


def printLine(nbEtoile):
    print("*" * nbEtoile + "D" * (n - 2 * nbEtoile) + "*" * nbEtoile)


for nbEtoile in range(-n // 2 + 1, n // 2 + 1):
    printLine(abs(nbEtoile))
