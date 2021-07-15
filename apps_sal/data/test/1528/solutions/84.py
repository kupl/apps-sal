N,X = list(map(int,input().split()))

burgerLengthList = [[] for i in range(51)]
for i in range(51):
    burgerLengthList[i].append(2 ** (i + 2) - 3)
    burgerLengthList[i].append(2 ** (i + 1) - 1)

def pNumber(level, number):
    if level == 0:
        return 1
    if number == 1:
        return 0
    if number <= burgerLengthList[level][0] // 2:
        return pNumber(level - 1, number - 1)
    elif number == burgerLengthList[level][0] // 2 + 1:
        return pNumber(level - 1, number - 1) + 1
    else:
        return burgerLengthList[level - 1][1] + 1 + pNumber(level - 1, number - burgerLengthList[level - 1][0] - 2)

print(pNumber(N, X))
