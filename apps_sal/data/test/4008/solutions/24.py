N, K = map(int, input().split())

arr = list(map(int, input().split()))

cDict = dict()


isFine = True

for a in arr:
    if a not in cDict: cDict[a] = 1
    else: cDict[a] += 1
    
    if cDict[a] > K:
        isFine = False
        break
    
if not isFine:
    print("NO")
else:
    print("YES")
    fDict = dict()
    lastC = 0
    for c in cDict:
        fDict[c] = cDict[c] + lastC
        lastC = fDict[c]
        
    ansArr = []
    for a in arr:
        ansArr.append(fDict[a])
        fDict[a] -= 1
    
    for an in ansArr:
        print(an % K + 1, end = ' ')
        
