D,G = list(map(int,input().split()))
pc = []
for i in range(D):
    pc.append(list(map(int,input().split())))

scoreList = [0 for i in range(D)]

for i in range(D):
    scoreList[i] = (i + 1) * 100 * pc[i][0] + pc[i][1]

choiceList = [[] for i in range(2 ** D)]
for i in range(2 ** D):
    for j in range(D):
        choiceList[i].append(i // (2 ** j) % 2)

minCount = 10 ** 8
for choice in choiceList:
    score = 0
    count = 0
    for i in range(len(choice)):
        if choice[i] == 1:
            score += scoreList[i]
            count += pc[i][0]
    for j in range(D):
        countTmp = count
        extraScore = (j + 1) * 100 * pc[j][0]
        delta = G - score
        if delta < 0:
            countTmp = count
        elif delta == 0:
            countTmp = count
        elif delta > 0:
            if delta <= extraScore and choice[j] == 0:
                countTmp += delta // ((j + 1) * 100)
                if delta % ((j + 1) * 100) > 0:
                    countTmp += 1
            else:
                countTmp = 10 ** 8
        if countTmp < minCount:
            minCount = countTmp
print(minCount)
