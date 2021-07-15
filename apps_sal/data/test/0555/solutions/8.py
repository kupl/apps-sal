x = list(input())
leadzero = True
for i in range(len(x)):
	s = int(x[i])
	if s > (9-s):
		if not (s == 9 and leadzero):
			x[i] = str(9-s)
	if int(x[i]) != 0:
		leadzero = False

print("".join(x))

