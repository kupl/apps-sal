import re
table = []
for _ in range(8):
    table.append(input())

ocrA = []
ocrB = []
A = 8
B = 8

for i in range(8):
    for j in range(8):
        if table[i][j] == "W":
            ocrA.append(j)
        elif table[i][j] == "B":
            ocrB.append(j)

    while ocrA != []:
        asteps = 0
        for j in range(i - 1, -1, -1):
            if table[j][ocrA[0]] != ".":
                asteps = -1
                break
            asteps += 1
        if asteps != -1 and asteps < A:
            A = asteps
        ocrA.pop(0)

    while ocrB != []:
        bsteps = 0
        for j in range(i + 1, 8):
            if table[j][ocrB[0]] != ".":
                bsteps = -1
                break
            bsteps += 1
        if bsteps != -1 and bsteps < B:
            B = bsteps
        ocrB.pop(0)

if A <= B:
    print("A")
else:
    print("B")
