S=input()
kisu=["R","U","D"]
gusu=["L","U","D"]


for i in range(len(S)):
	if (i+1)%2==0 and S[i] in gusu:
		continue
	elif (i+1)%2!=0 and S[i] in kisu:
		continue
	else:
		print("No")
		return

print("Yes")
