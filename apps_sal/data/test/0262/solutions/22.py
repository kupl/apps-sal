n = int(input())
arr = []
nullRow = nullCol = 0
for i in range(n):
    arr.append(list())
    for j, x in enumerate(list(map(int, input().split()))):
        arr[i].append(x)
        if x == 0:
            nullRow = i
            nullCol = j
arrT = list(zip(*arr))
sumRow = sum(arr[0 if nullRow != 0 or n == 1 else 1])
sumCol = sum(arrT[0 if nullCol != 0 or n == 1 else 1])
guessByRow = 0
guessByCol = 0
solvable = True
for i in range(n):
    currSum = sum(arr[i])
    if i == nullRow:
        guessByRow = sumRow - currSum 
    elif currSum != sumRow:
        solvable = False
for j in range(n):
    currSum = sum(arrT[j])
    if j == nullCol:
        guessByCol = sumCol - currSum 
    elif currSum != sumCol:
        solvable = False
if guessByRow != guessByCol or sumRow != sumCol:
    solvable = False
if solvable:
    arr[nullRow][nullCol] = guessByRow
sumDiagLeft = sumDiagRight = 0
for i in range(n):
    sumDiagRight += arr[i][n - i - 1]
    sumDiagLeft += arr[i][i]
if sumDiagLeft != sumDiagRight or sumRow != sumDiagLeft:
    solvable = False
if n == 1:
    print(1)
elif solvable and guessByRow > 0:
    print(guessByRow)
else:
    print(-1)
