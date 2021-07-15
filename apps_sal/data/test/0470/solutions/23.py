
cartes=list(map(int,input().split()))
somme=sum(cartes)
nbOccurence=[0]*100
enleverMax=0
for carte in cartes:
	nbOccurence[carte-1]+=1

for numeroCarte,nombre in enumerate(nbOccurence):
	
	nombreEnlever=min(3,nombre)
	if nombre>=2 and (numeroCarte+1)*nombreEnlever>enleverMax:
		enleverMax=(numeroCarte+1)*nombreEnlever

print(somme-enleverMax)
		

