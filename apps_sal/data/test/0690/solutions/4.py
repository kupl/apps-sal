#Soroban

n = input()
soroban = ""
for i in range(len(n)):
	digit = int(n[len(n)-i-1])
	soroban = ""
	if digit >= 5:
		soroban += "-O|"
		digit = digit - 5
	else:
		soroban += "O-|"
	if digit == 0:
		soroban += "-OOOO"
	elif digit == 1:
		soroban += "O-OOO"
	elif digit == 2:
		soroban += "OO-OO"
	elif digit == 3:
		soroban += "OOO-O"
	elif digit == 4:
		soroban += "OOOO-"
	print(soroban)

