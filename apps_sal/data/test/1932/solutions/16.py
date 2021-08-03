n = int(input())
o = 0
for i in range(n):
    s = input()
    if s == "Tetrahedron":
        o += 4
    elif s == "Cube":
        o += 6
    elif s == "Octahedron":
        o += 8
    elif s == "Dodecahedron":
        o += 12
    else:
        o += 20
print(o)
