n = int(input())
a = list(map(int, str(input()).split()))
minNumber = min(a)
sumA = minNumber * n
for i in range(n):
    a[i] -= minNumber
hasGoRound = False
isCounting = False
index = 0
count = 0
maxCount = 0
while True:
    if a[index] != 0 and (not isCounting):
        isCounting = True
    if a[index] != 0 and isCounting:
        count += 1
    else:
        if maxCount < count:
            maxCount = count
        if hasGoRound:
            break
        isCounting = False
        count = 0
    index += 1
    if index == n:
        index = 0
        hasGoRound = True
print(sumA + maxCount)
