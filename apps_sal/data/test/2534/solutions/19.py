R, C = map(int, input().split())
MAT = []
for r in range(R):
    MAT.append(list(map(int, input().split())))

colMax = []

for c in range(C):
    maxi = -1
    for r in range(R):
        if MAT[r][c] > maxi:
            maxi = MAT[r][c]
    colMax.append(maxi)

rowMin = []
for r in range(R):
    mini = MAT[r][0]
    for c in range(1, C):
        if MAT[r][c] < mini:
            mini = MAT[r][c]
    rowMin.append(mini)

noGuess = False
element = -1
for i in rowMin:
    if i in colMax:
        element = i
        noGuess = True
        break

if(noGuess):
    print(element)
else:
    print("GUESS")
