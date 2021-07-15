i = input()
i = int(i)
v = 0
g = 2
s = 4
while g <= i:
	while s <= i:
		v = v + int(s / g * 4)
		s = s + g
	g = g + 1
	s = g * 2
print(str(v))
