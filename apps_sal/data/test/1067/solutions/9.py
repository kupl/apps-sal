import math
n = int(input())
list1 = input().split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
total = 0
numNeg = 0
wiggle = False
for i in range(len(list1)):
    if list1[i] >= 1:
        total += list1[i] - 1
    elif list1[i] <= -1:
        total += -1 - list1[i]
        numNeg += 1
    else:
        total += 1
        wiggle = True
if wiggle:
    print(total)
elif numNeg % 2 == 1:
    print(total + 2)
else:
    print(total)
