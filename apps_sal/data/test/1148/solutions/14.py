n = int(input())
a = list(map(int, str(input()).split()))

# print('n', n)
# print('a', a)

minNumber = min(a)
sumA = minNumber * n

# print('sumA', sumA)

for i in range(n):
    a[i] -= minNumber

# print('a', a)

hasGoRound = False
isCounting = False
index = 0
count = 0
maxCount = 0
while True:
    # print('\ta', a[index])
    if a[index] != 0 and not isCounting:
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
# print('maxCount', maxCount)
print(sumA + maxCount)
