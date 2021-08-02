d = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20
}
n = int(input())
r = 0
for _ in range(n):
    r += d[input()]

print(r)
