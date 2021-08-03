problems, days = list(map(int, input().split(" ")))
difficulties = list(map(int, input().split(" ")))

copyDifficulties = difficulties.copy()
copyDifficulties.sort()
maxValues = {}

for i in range(days):
    if copyDifficulties[problems - 1 - i] in maxValues:
        maxValues[copyDifficulties[problems - i - 1]] += 1
    else:
        maxValues[copyDifficulties[problems - i - 1]] = 1

gained = 0
solved = []
solvedDay = 0
for i in range(problems):
    solvedDay += 1
    if difficulties[i] in maxValues and maxValues.get(difficulties[i]) >= 1:
        gained += difficulties[i]
        maxValues[difficulties[i]] -= 1
        solved.append(solvedDay)
        solvedDay = 0
solved[len(solved) - 1] += problems - sum(solved)
print(gained)
res = " "
for i in solved:
    res += str(i) + " "
print(res.strip())
