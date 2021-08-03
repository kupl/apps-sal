import copy


def DeleteRepetitionsIn(Array):
    AlreadyRead = {}
    index = 0
    ConstantArray = copy.deepcopy(Array)
    for a in range(len(ConstantArray)):
        if Array[index] not in AlreadyRead:
            AlreadyRead[Array[index]] = ""
            index += 1
            continue
        Array = Array[0:index] + Array[index + 1:len(Array)]

    return Array


def DeleteRepetitionsIn2(Array):
    AlreadyRead = {}
    for elem in Array:
        if elem in AlreadyRead:
            continue
        AlreadyRead[elem] = ""
    return list(AlreadyRead)


Results = []
ArraysNumber = int(input())
for e in range(ArraysNumber):
    AbsolutelyUselessNumber = int(input())
    Array = list(map(int, input().split()))
    if len(Array) == 1:
        Results.append(0)
        continue

    # print(Array)
    TheRightOrder = DeleteRepetitionsIn2(Array)
    TheRightOrder.sort()
    TheCurrentOrder = {}
    for i in range(len(Array)):
        if Array[i] not in TheCurrentOrder:
            TheCurrentOrder[Array[i]] = [i, i]
            continue
        TheCurrentOrder[Array[i]][1] = i

    # print(TheRightOrder)
    # print(TheCurrentOrder)
    # print(Array)

    TheCurrentResult = 1
    TheMaxResult = 1
    for i in range(len(TheRightOrder)):
        #print("a =", TheCurrentResult)
        #print("b =", TheMaxResult)
        if i == len(TheRightOrder) - 1:
            if TheCurrentResult >= TheMaxResult:
                TheMaxResult = TheCurrentResult
            continue
        if TheCurrentOrder[TheRightOrder[i]][1] > TheCurrentOrder[TheRightOrder[i + 1]][0]:
            if TheCurrentResult >= TheMaxResult:
                TheMaxResult = TheCurrentResult

            TheCurrentResult = 1
            continue

        TheCurrentResult += 1

    Results.append(len(TheRightOrder) - TheMaxResult)

for i in Results:
    print(i)
