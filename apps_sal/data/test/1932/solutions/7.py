#!/bin/python3

import sys
n = int(input())
d = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20};
ans = 0
for i in range(n):
    name = input()
    ans += d[name];
print(ans)
