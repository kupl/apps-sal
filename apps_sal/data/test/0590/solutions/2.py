from sys import stdin, stdout
n = int(stdin.readline().rstrip())
a = list(map(int, stdin.readline().rstrip().split()))
aSet = set(a)
aMinus = set(range(1, n + 1)) - aSet
minusList = sorted(list(aMinus), reverse=True)
used = set()
countDict = {x: 0 for x in aSet}
for x in a:
    countDict[x] += 1
finalList = a
for i in range(n):
    x = a[i]
    if x in used:
        finalList[i] = minusList.pop()
    elif countDict[x] == 1:
        continue
    elif x < minusList[-1]:
        used.add(x)
    else:
        countDict[x] -= 1
        finalList[i] = minusList.pop()
print(len(aMinus))
print(' '.join(map(str, finalList)))
