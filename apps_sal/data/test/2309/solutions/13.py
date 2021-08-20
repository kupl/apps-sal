vowelList = ['a', 'e', 'i', 'o', 'u']
r = int(input())
stringArr = []
for i in range(r):
    string = input()
    properties = []
    properties.append(string)
    backStr = string[::-1]
    numVowel = 0
    for j in range(len(string)):
        if backStr[j] in vowelList:
            if numVowel == 0:
                properties.append(backStr[j])
            numVowel += 1
    properties.append(numVowel)
    stringArr.append(properties)
stringArr.sort(key=lambda arr: arr[2])
n = 1
left = 0
equalNumVowels = []
correspondingSecondPairs = []
correspondingFirstPairs = []
currentArr = []
for i in range(r):
    if stringArr[i][2] > n:
        equalNumVowels.append(currentArr)
        n = stringArr[i][2]
        currentArr = []
    currentArr.append(stringArr[i])
equalNumVowels.append(currentArr)
for ar in equalNumVowels:
    aArr = []
    eArr = []
    iArr = []
    oArr = []
    uArr = []
    for item in ar:
        if item[1] == 'a':
            aArr.append(item)
        elif item[1] == 'e':
            eArr.append(item)
        elif item[1] == 'i':
            iArr.append(item)
        elif item[1] == 'o':
            oArr.append(item)
        else:
            uArr.append(item)
    while len(aArr) > 1:
        m = aArr.pop()
        n = aArr.pop()
        correspondingSecondPairs.append([m, n])
    while len(eArr) > 1:
        m = eArr.pop()
        n = eArr.pop()
        correspondingSecondPairs.append([m, n])
    while len(iArr) > 1:
        m = iArr.pop()
        n = iArr.pop()
        correspondingSecondPairs.append([m, n])
    while len(oArr) > 1:
        m = oArr.pop()
        n = oArr.pop()
        correspondingSecondPairs.append([m, n])
    while len(uArr) > 1:
        m = uArr.pop()
        n = uArr.pop()
        correspondingSecondPairs.append([m, n])
    leftOver = []
    if len(aArr) == 1:
        leftOver.append(aArr[0])
    if len(eArr) == 1:
        leftOver.append(eArr[0])
    if len(iArr) == 1:
        leftOver.append(iArr[0])
    if len(oArr) == 1:
        leftOver.append(oArr[0])
    if len(uArr) == 1:
        leftOver.append(uArr[0])
    while len(leftOver) > 1:
        m = leftOver.pop()
        n = leftOver.pop()
        correspondingFirstPairs.append([m, n])
print(min(len(correspondingSecondPairs), len(correspondingFirstPairs) + (len(correspondingSecondPairs) - len(correspondingFirstPairs)) // 2))
while len(correspondingFirstPairs) >= 1 and len(correspondingSecondPairs) >= 1:
    a = correspondingFirstPairs.pop()
    b = correspondingSecondPairs.pop()
    print(str(a[0][0]) + ' ' + str(b[0][0]) + '\n' + str(a[1][0]) + ' ' + str(b[1][0]))
while len(correspondingSecondPairs) >= 2:
    a = correspondingSecondPairs.pop()
    b = correspondingSecondPairs.pop()
    print(str(a[0][0]) + ' ' + str(b[0][0]) + '\n' + str(a[1][0]) + ' ' + str(b[1][0]))
