s = input()
blocks = []
evenA = [0]
oddA = [0]
evenB = [0]
oddB = [0]
even = True
for x in s:
    evenA.append(evenA[-1])
    oddA.append(oddA[-1])
    evenB.append(evenB[-1])
    oddB.append(oddB[-1])
    if x == 'a':
        if even:
            evenA[-1] += 1
        else:
            oddA[-1] += 1
    elif even:
        evenB[-1] += 1
    else:
        oddB[-1] += 1
    even = not even
even = True
totalE = 0
totalO = 0
for x in range(len(s)):
    if s[x] == 'a':
        if x % 2 == 0:
            totalE += evenA[-1] - evenA[x]
            totalO += oddA[-1] - oddA[x]
        else:
            totalE += oddA[-1] - oddA[x]
            totalO += evenA[-1] - evenA[x]
    elif x % 2 == 0:
        totalE += evenB[-1] - evenB[x]
        totalO += oddB[-1] - oddB[x]
    else:
        totalE += oddB[-1] - oddB[x]
        totalO += evenB[-1] - evenB[x]
print(totalO, totalE)
