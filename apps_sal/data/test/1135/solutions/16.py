input()
scrambled = input().strip()
if len(scrambled) % 2:
	parity	=1
else:
	parity	=0
unscrambled = ""
while len(scrambled) > 0:
	if parity == 0:
		unscrambled	= scrambled[0] + unscrambled
		parity=1
	else: 
		unscrambled	+= scrambled[0]
		parity	=0
	scrambled = scrambled[1:]
print(unscrambled)
