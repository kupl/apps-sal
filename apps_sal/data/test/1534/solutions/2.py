from sys import stdin, stdout
s = stdin.readline().rstrip()
n = len(s)
aCount = 0
bCount = 0
aList = [0]
bList = [0]
for i in range(n):
    if s[i] == 'a':
        aCount += 1
        aList.append(aCount)
        bList.append(bCount)
    else:
        bCount += 1
        aList.append(aCount)
        bList.append(bCount)
bestScore = 0
for i in range(n + 1):
    for j in range(i, n + 1):
        score = 0
        score += aList[i]
        score += bList[j] - bList[i]
        score += aCount - aList[j]
        if score > bestScore:
            bestScore = score
print(bestScore)
