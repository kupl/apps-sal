n = int(input())

r = 0
for i in range(n):
	s = input().strip()
	if s == 'Tetrahedron':
		r += 4
	elif s == 'Cube':
		r += 6
	elif s == 'Octahedron':
		r += 8
	elif s == 'Dodecahedron':
		r += 12
	elif s == 'Icosahedron':
		r += 20

print(r)
