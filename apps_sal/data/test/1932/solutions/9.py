import math
import itertools


def ria():
    return [int(i) for i in input().split()]


mp = {'tetrahedron': 4,
      'cube': 6,
      'octahedron': 8,
      'dodecahedron': 12,
      'icosahedron': 20}

sz = ria()[0]
suma = 0
for i in range(sz):
    suma += mp[str(input()).lower()]
print(suma)
