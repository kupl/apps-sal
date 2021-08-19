from sys import stdin


def main():
    inp = stdin
    L = list()
    for i in range(3):
        dig = inp.readline().strip()
        L.append(dig)
    L = list(map(int, L))
    cont = 1
    fin = 0
    while cont != 5:
        if cont == 1:
            mayor = sum(L)
        elif cont == 2:
            mayor = L[0]
            for i in range(1, 3):
                mayor = mayor * L[i]
        elif cont == 3:
            mid = L[0:-1]
            suma = sum(mid)
            mayor = suma * L[-1]
        elif cont == 4:
            mid = L[1:]
            suma = sum(mid)
            mayor = suma * L[0]
        elif cont == 5:
            suma = L[0] + L[2]
            mayor = suma * L[1]
        cont += 1
        if mayor > fin:
            fin = mayor
    print(fin)


main()
