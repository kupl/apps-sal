n = input()

for i in range(len(n)):
	if (n[i] == '1' or n[i] == '2'):
		print("No")
		return
	elif ((n[i] == '3' or n[i] == '7') and n[-i - 1] != n[i]):
		print("No")
		return
	elif (n[i] == '4' and n[-i - 1] != '6'):
		print("No")
		return
	elif (n[i] == '6' and n[-i - 1] != '4'):
		print("No")
		return
	elif (n[i] == '5' and n[-i - 1] != '9'):
		print("No")
		return
	elif (n[i] == '9' and n[-i - 1] != '5'):
		print("No")
		return
	elif (n[i] == '8' and n[-i - 1] != '0'):
		print("No")
		return
	elif (n[i] == '0' and n[-i - 1] != '8'):
		print("No")
		return
	
print("Yes")
