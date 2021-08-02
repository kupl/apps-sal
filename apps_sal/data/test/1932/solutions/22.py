__author__ = 'zihaozhu'
from sys import stdin

cases = int(stdin.readline())

total = 0
for i in range(cases):
    shape = stdin.readline().rstrip()
    if shape == "Tetrahedron":
        total += 4
    elif shape == "Cube":
        total += 6
    elif shape == "Octahedron":
        total += 8
    elif shape == "Dodecahedron":
        total += 12
    elif shape == "Icosahedron":
        total += 20
print(total)
