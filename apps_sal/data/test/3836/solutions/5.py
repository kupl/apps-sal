
n = int(input())
# 00 = 0, 01 = 1, 10 = 2, 11 = 3
tonumber = {'00': 0, '01': 1, '10': 2, '11': 3}
people = [[], [], [], []]
for i in range(n):
    s, a = input().split()
    s, a = tonumber[s], int(a)
    people[s].append(a)
people[0].sort(reverse=True)
people[1].sort(reverse=True)
people[2].sort(reverse=True)
# print(people)
totalInfluence = sum(people[3])
totalPeople = len(people[3])
support = [len(people[3]), len(people[3])]
minLen = min(len(people[1]), len(people[2]))
for i in range(minLen):
    totalInfluence += people[1][i] + people[2][i]
    totalPeople += 2
    support[0] += 1
    support[1] += 1
longer = 0
longerIndex = 2
if minLen == len(people[1]):
    longer = 0
    longerIndex = 2
else:
    longer = 1
    longerIndex = 1
indices = [0, minLen]
allEmpty = [len(people[0]), len(people[longerIndex])]
#print(longer, longerIndex, minLen, indices, allEmpty)
while indices != allEmpty:
    top = [-1, -1]
    if indices[0] != allEmpty[0]:
        top[0] = people[0][indices[0]]
    if indices[1] != allEmpty[1]:
        top[1] = people[longerIndex][indices[1]]
    if top[0] > top[1]:
        if support[longer] >= (totalPeople + 1) / 2 and support[not longer] >= (totalPeople + 1) / 2:
            #print(str(support[longer]) + ' ' +  str((totalPeople + 1) / 2) + ';' + str(support[not longer]) + ' ' +  str((totalPeople + 1) / 2))
            totalInfluence += top[0]
            totalPeople += 1
            indices[0] += 1
        else:
            indices[0] += 1
    else:
        if support[not longer] >= (totalPeople + 1) / 2:
            totalInfluence += top[1]
            totalPeople += 1
            support[longer] += 1
            indices[1] += 1
        else:
            indices[1] += 1
    #print(top, support, totalInfluence, totalPeople)

if totalPeople != 0:
    print(totalInfluence)
else:
    print(0)
