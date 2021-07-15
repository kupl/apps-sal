row, col = map(int, input().split())
m = [[int(x) for x in input().split()] for y in range(row)]

minL = []
maxL = []
ans = []

for i in range(row):
    minVal = 10**12
    for j in range(col):
        if(minVal>=m[i][j]):
            minVal = m[i][j]
    minL.append(minVal)

for i in range(col):
    maxVal = 0
    for j in range(row):
        if(maxVal<=m[j][i]):
            maxVal = m[j][i]
    maxL.append(maxVal)

for i in minL:
    for j in maxL:
        if i == j:
            ans.append(i)
if ans:
    print(max(ans))
else:
    print('GUESS')
