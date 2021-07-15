tommy, banban = list(map(int, input().split(" ")))
allTommy = sorted(list(map(int, input().split(" "))))
allBanban = sorted(list(map(int, input().split(" "))))
allValues = []
for i in allTommy:
    for j in allBanban:
        allValues.append([i*j, i, j])
allValues.sort()
i = 0
while i < len(allTommy):
    if allTommy[i] == allValues[-1][1]:
        allTommy.pop(i)
        break
    i += 1
newValues = []
for i in allTommy:
    for j in allBanban:
        newValues.append(i*j)
newValues.sort()
print(newValues[-1])
