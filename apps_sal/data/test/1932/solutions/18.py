a = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
n = int(input())
s = 0
for _ in range(0, n):
    s += a[input()]
print(s)
