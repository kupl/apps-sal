n = int(input())
d = 0
for i in range(n):
    s = input()
    if(s == "Tetrahedron"):
        d = d + 4
    elif(s == "Cube"):
        d = d + 6
    elif(s == "Octahedron"):
        d = d + 8
    elif(s == "Dodecahedron"):
        d = d + 12
    else: d = d + 20
print(d)
