letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


def getPalindrome(counts):
    returnString = ''
    for i in range(len(counts)):
        if counts[i] >= 2:
            for j in range(counts[i] // 2):
                counts[i] -= 2
                returnString += letters[i]
    for i in range(len(counts)):
        if counts.count(0) == 26:
            return returnString + returnString[::-1]
        elif counts[i] == 1 and counts.count(0) == 25:
            return returnString + letters[i] + returnString[::-1]


def changeCounts(counts):
    allEven = True
    for i in counts:
        if i % 2 == 1:
            allEven = False
    if allEven == True:
        return counts
    else:
        for i in range(len(counts)):
            if counts[25 - i] % 2 == 1:
                for j in range(len(counts)):
                    if j == 25 - i:
                        return counts
                    elif counts[j] % 2 == 1:
                        counts[j] += 1
                        counts[25 - i] -= 1
                        break
        return counts


inputArg = list(input())
counts = []
for i in letters:
    counts.append(inputArg.count(i))
counts = changeCounts(counts)
print(getPalindrome(counts))
