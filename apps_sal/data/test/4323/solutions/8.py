nbMusiques, taille = map(int, input().split())
tableau = []
somme = 0

for i in range(nbMusiques):
    avant, apres = map(int, input().split())
    somme += avant
    tableau.append(avant - apres)

tableau.sort()

if somme <= taille:
    print(0)

else:
    for i in range(nbMusiques):
        somme -= tableau[nbMusiques - 1 - i]

        if somme <= taille:
            print(i + 1)
            break

    if somme > taille:
        print(-1)
