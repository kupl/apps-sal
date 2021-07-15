n = int(input())
s = 0
for i in range(n):
	current = input()
	if current == "Tetrahedron":
		s += 4
	elif current == "Cube":
		s += 6
	elif current == "Octahedron":
		s += 8
	elif current == "Dodecahedron":
		s += 12
	else:
		s += 20
print(s)

