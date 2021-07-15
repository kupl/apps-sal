n = int(input())
sushi = [int(x) for x in input().strip().split(" ")]

newList = []
prev = sushi[0]
newList.append(1)

for type in sushi[1:]:
    if prev != type:
        newList.append(1)
    else:
        newList[len(newList) - 1] += 1
    prev = type

maxSushi = 0
for i, j in zip(newList, newList[1:]):
    maxSushi = max(maxSushi, min(i, j))

print(maxSushi * 2)

