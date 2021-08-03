

def estBissextile(annee):
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        return True
    return False


annee = int(input())

if not estBissextile(annee):
    compteur = 1
    annee += 1
    while compteur % 7 != 0 or estBissextile(annee):
        if estBissextile(annee):
            compteur += 2
        else:
            compteur += 1
        annee += 1
else:
    compteur = 2
    annee += 1
    while compteur % 7 != 0 or not estBissextile(annee):
        if estBissextile(annee):
            compteur += 2
        else:
            compteur += 1
        annee += 1

print(annee)
