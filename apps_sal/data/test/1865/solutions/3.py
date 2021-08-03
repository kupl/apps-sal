n = int(input(''))

arvud = input('').split()
arvud = list(map(int, arvud))
swaps = []
begin = 0

for i in range(n):
    mini = min(arvud)
    index = arvud.index(mini)
    if index != 0:
        arvud[0], arvud[index] = arvud[index], arvud[0]
        swaps.append((begin, index + begin))

    arvud.pop(0)
    begin += 1


print(len(swaps))
for i in range(len(swaps)):
    print(swaps[i][0], " ", swaps[i][1])
