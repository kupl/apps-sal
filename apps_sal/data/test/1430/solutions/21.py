N, K = list(map(int, input().split()))
S = input()

beforeChar = S[0]
sectionList = []
count = 0
for i in range(N):
    if S[i] == beforeChar:
        count += 1
    else:
        sectionList.append([beforeChar, count])
        count = 1
        beforeChar = S[i]
sectionList.append([beforeChar, count])

sectionNumber = len(sectionList)
zeroSectionNumber = 0
oneSectionNumber = 0
if sectionNumber % 2 == 0:
    zeroSectionNumber = sectionNumber // 2
    oneSectionNumber = sectionNumber // 2
else:
    if sectionList[0][0] == '0':
        zeroSectionNumber = sectionNumber // 2 + 1
        oneSectionNumber = sectionNumber // 2
    else:
        zeroSectionNumber = sectionNumber // 2
        oneSectionNumber = sectionNumber // 2 + 1

if zeroSectionNumber <= K:
    print(N)
    return

sumLengthList = []
sumLength = 0
for i in range(sectionNumber):
    sumLength += sectionList[i][1]
    sumLengthList.append(sumLength)


def sumLengthByRange(rangeStartSection, rangeEndSection):
    if rangeStartSection == 0:
        return sumLengthList[rangeEndSection]
    else:
        return sumLengthList[rangeEndSection] - sumLengthList[rangeStartSection - 1]


startSection = 0
endSection = 0
lengthList = []
if sectionList[0][0] == '1':
    endSection = K * 2
else:
    endSection = K * 2 - 1
    lengthList.append(sumLengthByRange(startSection, endSection))
    startSection = 1
    endSection += 2
while endSection < sectionNumber:
    lengthList.append(sumLengthByRange(startSection, endSection))
    startSection += 2
    endSection += 2
if sectionList[-1][0] == '0':
    endSection -= 1
    lengthList.append(sumLengthByRange(startSection, endSection))

print(max(lengthList))
