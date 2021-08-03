

nbLig, nbCol = list(map(int, input().split()))
couleurs = ["C", "M", "Y", "W", "G", "B"]
compteur = [0] * 6
for lig in range(nbLig):
    ligne = input().split()
    for element in ligne:
        compteur[couleurs.index(element)] += 1

if compteur[0] != 0 or compteur[1] != 0 or compteur[2] != 0:
    print("#Color")
else:
    print("#Black&White")
