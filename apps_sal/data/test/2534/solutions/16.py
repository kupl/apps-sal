
r, c = (map(int, input().strip().split()))


matrix = []
minRow = []
for i in range(r):
    arr = list(map(int, input().strip().split()))
    minRow.append(min(arr))
    matrix.append(arr)
flag = 1
maxCol = []
for j in range(c):
    maxi = -1
    for i in range(r):
        maxi = max(maxi, matrix[i][j])
    maxCol.append(maxi)

for i in range(r):
    n = minRow[i]

    for j in range(c):
        if matrix[i][j] == n and maxCol[j] == n:

            flag = 0
            break
    if flag == 0:
        break

if flag == 0:

    print(n)
else:
    print("GUESS")
