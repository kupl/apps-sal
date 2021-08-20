from sys import stdin
phrase = input()
lettreActuelle = 0
total = 0
for lettre in phrase:
    gauche = (ord(lettre) - ord('a') - lettreActuelle) % 26
    droite = (lettreActuelle - ord(lettre) + ord('a')) % 26
    rotation = min(gauche, droite)
    total += rotation
    lettreActuelle = ord(lettre) - ord('a')
print(total)
