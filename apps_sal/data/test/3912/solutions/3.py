n = int(input())
string = input()
char = []
charPair = []
charImpair = []
for car in string:
	if car not in char:
		z = string.count(car)
		while z>1:
			charPair.append(car)
			z-=2
		if(z==1):
			charImpair.append(car)
		char.append(car)
if len(charImpair) ==0 :
	String1 = ''
	for x in charPair:
		String1+= x
	if len(charImpair) ==1 :
		String1 += charImpair[0]
	for x in charPair[::-1]:
		String1 += x
	print('1')
	print(String1)
else :
	nbPalin = len(charImpair)
	while len(charPair)%nbPalin != 0 : 
		nbPalin += 2
		charImpair.append(charPair[-1])
		charImpair.append(charPair[-1])
		del(charPair[-1])
	lenPalindrome = n/nbPalin
	Palin = []
	for i in range(nbPalin):
		String2 = ''
		indice = i * int(((lenPalindrome-1)/2))
		for x in charPair[indice : int(indice + ((lenPalindrome-1)/2))]:
			String2 += x
		String2 += charImpair[i]
		for x in range(indice + int(((lenPalindrome-1)/2))-1, indice-1 ,-1):   #   charPair[i + int(((lenPalindrome-1)/2))-1: i-1 :-1]:
			String2 += charPair[x]	
		Palin.append(String2)
		
	print(nbPalin)
	String3 = ' '.join(Palin)
	print(String3)


