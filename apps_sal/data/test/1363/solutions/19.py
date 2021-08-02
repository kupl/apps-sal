s = input().split()
l = sum([int(i) for i in s])

data = []
for j in range(3):
    data += [[int(i) for i in input().split()]]
    data[j] += [100001]
    data[j].sort()

cursor = [0, 0, 0]
posCnt = [0, 0, 0]
lowerBound = 0
upperBound = 0

finalCounter = 0

mainQueue = []
player = []

i = 0
while i < l:

    player = min([data[0][cursor[0]], 0], [data[1][cursor[1]], 1], [data[2][cursor[2]], 2])

    if lowerBound == i:
        mainQueue += [player]
        cursor[player[1]] += 1
        upperBound = mainQueue[lowerBound][0] * 2
        posCnt[player[1]] += 1
    else:
        if player[0] > upperBound:
            if posCnt[0] > 0 and posCnt[1] > 1 and posCnt[2] > 2:

                posCnt[mainQueue[lowerBound][1]] -= 1
                if mainQueue[lowerBound][1] == 0:
                    finalCounter += posCnt[1] * (posCnt[1] - 1) * posCnt[2] * (posCnt[2] - 1) * (posCnt[2] - 2) // 12
                elif mainQueue[lowerBound][1] == 1:
                    finalCounter += posCnt[0] * posCnt[1] * posCnt[2] * (posCnt[2] - 1) * (posCnt[2] - 2) // 6
                else:
                    finalCounter += posCnt[0] * posCnt[1] * (posCnt[1] - 1) * posCnt[2] * (posCnt[2] - 1) // 4

                lowerBound += 1
                upperBound = mainQueue[lowerBound][0] * 2
            else:
                posCnt[mainQueue[lowerBound][1]] -= 1
                lowerBound += 1
                if lowerBound < i:
                    upperBound = mainQueue[lowerBound][0] * 2
            i -= 1

        else:
            mainQueue += [player]
            cursor[player[1]] += 1
            posCnt[player[1]] += 1
    i += 1


while posCnt[0] > 0 and posCnt[1] > 1 and posCnt[2] > 2:

    posCnt[mainQueue[lowerBound][1]] -= 1
    if not mainQueue[lowerBound][1]:
        finalCounter += posCnt[1] * (posCnt[1] - 1) * posCnt[2] * (posCnt[2] - 1) * (posCnt[2] - 2) // 12
    elif mainQueue[lowerBound][1] == 1:
        finalCounter += posCnt[0] * posCnt[1] * posCnt[2] * (posCnt[2] - 1) * (posCnt[2] - 2) // 6
    else:
        finalCounter += posCnt[0] * posCnt[1] * (posCnt[1] - 1) * posCnt[2] * (posCnt[2] - 1) // 4

    lowerBound += 1

print(finalCounter)
