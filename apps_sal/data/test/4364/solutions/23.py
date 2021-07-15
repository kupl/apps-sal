S = input()

first = int(S[0:2])
last = int(S[2:4])

if (0 < first < 13):
	if (0 < last < 13):
		print("AMBIGUOUS")
	else:
		print("MMYY")
else:
	if (0 < last < 13):
		print("YYMM")
	else:
		print("NA")
