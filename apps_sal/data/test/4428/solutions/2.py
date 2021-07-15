length = int(input())
numbers = list(map(int, input().split(" ")))

maxTotal = 0
totalLeft = 0
indexLeft = 0
totalRight = 0
indexRight = length - 1

while indexLeft <= indexRight:
    if totalLeft > totalRight:
        totalRight += numbers[indexRight]
        indexRight -= 1
    else:
        totalLeft += numbers[indexLeft]
        indexLeft += 1
    if totalRight == totalLeft:
        maxTotal = max(maxTotal, totalLeft)
print(maxTotal)

