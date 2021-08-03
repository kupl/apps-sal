data = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20
}
n = int(input())
ans = 0
for _ in range(0, n):
    s = input()
    ans = ans + data[s]
print(ans)
