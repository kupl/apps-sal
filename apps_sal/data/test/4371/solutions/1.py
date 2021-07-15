S = input()
min = 1000
for i in range(len(S) - 2):
	x = int(S[i:i+3])
	x = abs(753 - x)
	if min > x:
		min = x
print(min)
