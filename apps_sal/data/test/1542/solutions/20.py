from sys import stdin, stdout

nbMagasins = int(stdin.readline())
prix = list(map(int, stdin.readline().split()))
prix.sort()
q = int(stdin.readline())

for i in range(q):
    prixMax = int(stdin.readline())

    inf = 0
    sup = nbMagasins - 1

    while sup > inf:
        milieu = (inf + sup) // 2
        if prix[milieu] > prixMax:
            sup = milieu
        else:
            inf = milieu + 1

    if prixMax < prix[0]:
        print(0)
    elif prixMax >= prix[-1]:
        print(nbMagasins)
    else:
        print(inf)
