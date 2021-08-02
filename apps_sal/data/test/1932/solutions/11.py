d = {}
d['Tetrahedron'] = 4
d['Cube'] = 6
d['Octahedron'] = 8
d['Dodecahedron'] = 12
d['Icosahedron'] = 20

print(sum([d[input()] for _ in range(int(input()))]))
