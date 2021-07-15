n=int(input())
nombres=list(map(int,input().split()))

nombres.sort()

i=0
entierSuivant=1
while i!=n:
    if nombres[i]>entierSuivant:
        nombres[i]=entierSuivant
        entierSuivant+=1
    elif entierSuivant==nombres[i]:
        entierSuivant+=1
    i+=1

print(entierSuivant)
