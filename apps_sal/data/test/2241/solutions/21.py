import math
n = int(input())
aList = list(map(int,input().split()))
bList = list(map(int,input().split()))
joy = 0
for i in range(n):
    if bList[i] == 1:
        joy = joy - 1
    else:
        if bList[i] % 2 == 0:
            b1 = bList[i] / 2
            b2 = bList[i] / 2
        else:
            b1 = math.floor(bList[i] / 2)
            b2 = math.ceil(bList[i] / 2)
        if b2 <= aList[i]:
            joy = joy + b1 * b2
        else:
            joy = joy - 1
print(int(joy))
