from fractions import Fraction
from math import inf

n = int(input())
coords = []
for i in range(n):
    x, y = [int(c) for c in input().split(" ")]
    coords.append((x, y))

tangents = {}
for i1 in range(n):
    for i2 in range(i1+1, n):
        x1, y1 = coords[i1]
        x2, y2 = coords[i2]
        if x2 == x1:
            tangent = inf
            offset = x1
        else:
            tangent = Fraction(y2-y1, x2-x1)
            offset = - tangent * x1 + y1

        if tangent not in tangents: tangents[tangent] = set()
        tangents[tangent].add(offset)

tangentlen = {}
for tangent in tangents: tangentlen[tangent] = len(tangents[tangent])

summ = 0
for tangent in tangents: summ += tangentlen[tangent]

answer = 0
for t1 in tangents:
    answer += tangentlen[t1] * (summ - tangentlen[t1])
print(answer // 2)

