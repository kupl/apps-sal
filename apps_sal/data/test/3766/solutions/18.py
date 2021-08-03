from itertools import chain, combinations
from copy import deepcopy


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


n = int(input())
locations = input().split()
matrixG = [[0] * 5 for i in range(5)]
for i in locations:
    if i[0] == "R":
        matrixG[0][int(i[1]) - 1] += 1
    elif i[0] == "G":
        matrixG[1][int(i[1]) - 1] += 1
    elif i[0] == "B":
        matrixG[2][int(i[1]) - 1] += 1
    elif i[0] == "Y":
        matrixG[3][int(i[1]) - 1] += 1
    elif i[0] == "W":
        matrixG[4][int(i[1]) - 1] += 1

for i in list(powerset(list(range(10)))):
    matrix = deepcopy(matrixG)
    color = []
    value = []
    for j in i:
        if j <= 4:
            color.append(j)
        else:
            value.append(j)
    for v in value:
        for c in color:
            matrix[c][v - 5] = 0
        ctr = 0
        for r in range(5):
            if matrix[r][v - 5] == 0:
                ctr += 1
        if ctr == 4:
            for r in range(5):
                matrix[r][v - 5] = 0
    for c in color:
        if matrix[c].count(0) == 4:
            matrix[c] = [0] * 5
    ctr = 0
    for k in range(5):
        for j in range(5):
            if matrix[k][j] == 0:
                ctr += 1
    if ctr == 24:
        print(len(i))
        break
