[n, s] = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]

mistakes = 0

mistakes += (a[s-1] is not 0)
a[s - 1] = 0

numSuperiors = [0]*(2*100000+100)

for superiors in a:
    numSuperiors[superiors] += 1

cachedMistakes = 0

while numSuperiors[0] != 1:
    cachedMistakes += 1
    numSuperiors[0] -= 1

rightIndex = len(numSuperiors) - 1
leftIndex = 0
while True:
    while True:
        if numSuperiors[leftIndex] == 0 and cachedMistakes != 0:
            numSuperiors[leftIndex] += 1
            cachedMistakes -= 1
            mistakes += 1
        if numSuperiors[leftIndex] == 0:
            break
        leftIndex += 1
    while numSuperiors[rightIndex] == 0:
        rightIndex -= 1
    if leftIndex >= rightIndex:
        break
    numSuperiors[rightIndex] -= 1
    cachedMistakes += 1

print(mistakes)
