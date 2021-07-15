a=input()
alle = set()
alle.add(int(a))

while True:
	x = int(a)
	x += 1
	y = str(x)
	while y[-1] == "0":
		y = y[:-1]
	if int(y) in alle:
		break
	alle.add(int(y))
	a = y
print(len(alle))

