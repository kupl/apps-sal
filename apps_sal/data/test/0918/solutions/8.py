nm = list(map(int, input().split()))
largeDict = {}
for i in range(nm[1]):
    largeDict[i + 1] = {}
for i in range(nm[0]):
    tempList = input().split()
    largeDict[int(tempList[1])][tempList[0]] = int(tempList[2])
for i in range(nm[1]):
    aList = []
    newDict = {}
    aList = list(largeDict[i + 1].values())
    aList = sorted(aList)[len(aList) - 2:]
    for h in list(largeDict[i + 1].keys()):
        if largeDict[i + 1][h] in aList:
            newDict[h] = largeDict[i + 1][h]
    largeDict[i + 1] = newDict
    if len(list(largeDict[i + 1].keys())) > 2:
        print("?")
    else:
        print(" ".join(list(largeDict[i + 1].keys())))
