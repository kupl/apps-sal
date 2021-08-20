(N, A, B, C) = list(map(int, input().split()))
l = []
for i in range(N):
    l.append(int(input()))
choiceList = []
for i in range(4 ** N):
    choice = [-1 for i in range(N)]
    for j in range(N):
        choice[j] = i // 4 ** j % 4
    choiceList.append(choice)
minCost = 10 ** 9
for choice in choiceList:
    cost = 10 ** 9
    aList = []
    bList = []
    cList = []
    for i in range(N):
        if choice[i] == 1:
            aList.append(l[i])
        elif choice[i] == 2:
            bList.append(l[i])
        elif choice[i] == 3:
            cList.append(l[i])
    if len(aList) == 0 or len(bList) == 0 or len(cList) == 0:
        cost = 10 ** 9
    else:
        aCost = (len(aList) - 1) * 10 + abs(sum(aList) - A)
        bCost = (len(bList) - 1) * 10 + abs(sum(bList) - B)
        cCost = (len(cList) - 1) * 10 + abs(sum(cList) - C)
        cost = aCost + bCost + cCost
    if minCost > cost:
        minCost = cost
print(minCost)
