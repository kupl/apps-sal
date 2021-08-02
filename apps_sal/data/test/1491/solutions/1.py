from sys import stdin, stdout

n = int(stdin.readline().rstrip())
a = list(map(int, stdin.readline().rstrip().split()))
a.sort()

squareList = [i * i for i in range(int(1000000000**0.5) + 2)]

squareCount = 0
zeroCount = 0
lowerSquare = -1
upperSquare = 0
index = 0
distanceList = []
for x in a:
    while x > upperSquare:
        index += 1
        upperSquare = squareList[index]
        lowerSquare = squareList[index - 1]
    if x == upperSquare:
        squareCount += 1
        if x == 0:
            zeroCount += 1
    else:
        distanceList.append(min([upperSquare - x, x - lowerSquare]))
distanceList.sort()


change = 0
if squareCount > n // 2:
    nonZeroCount = squareCount - zeroCount
    if squareCount - n // 2 <= nonZeroCount:
        change = squareCount - n // 2
    else:
        change = nonZeroCount + 2 * (squareCount - n // 2 - nonZeroCount)
elif squareCount < n // 2:
    change = sum(distanceList[:n // 2 - squareCount])

print(change)
